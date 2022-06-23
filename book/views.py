from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.core.paginator import Paginator
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin

from .utils import RegisterOrLoginMixin
from .models import *
from .forms import *


def book_list(request):
    books = Book.objects.all()
    genres = Genre.objects.all()
    authors = Author.objects.all()

    search = request.GET.get('search', '')
    if search:
        books = Book.objects.filter(title__icontains=search)

    paginator = Paginator(books, settings.PAGINATOR_NUM)
    page_number = request.GET.get('page', 1)
    books = paginator.get_page(page_number)

    context = {
        'books': books,
        'genres': genres,
        'authors': authors,
    }
    return render(request, 'book/book_list.html', context)


def books_filter(request, slug):
    books = Book.objects.filter(genre__slug=slug)
    return render(request, 'book/books_filter.html', {'books': books})


def book_detail(request, slug):
    book = get_object_or_404(Book, slug__iexact=slug)
    return render(request, 'book/book_detail.html', {'book': book, 'detail': True})


def read_book(request, slug):
    book = get_object_or_404(Book, slug__iexact=slug)
    return render(request, 'book/read_book.html', {'book': book})


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    author_books = author.books.all()
    context = {
        'author': author,
        'author_books': author_books,
    }
    return render(request, 'book/author_detail.html', context)


class CreateBook(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request):
        form = CreateBookForm()
        return render(request, 'book/create_book.html', {'form': form})

    def post(self, request):
        bound_form = CreateBookForm(request.POST, request.FILES)
        if bound_form.is_valid():
            new_book = bound_form.save()
            return redirect(new_book.get_absolute_url())
        return render(request, 'book/create_book.html', {'form': bound_form})


class UpdateBook(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request, slug):
        book = get_object_or_404(Book, slug__iexact=slug)
        bound_form = CreateBookForm(instance=book)
        return render(request, 'book/book_update.html', {'form': bound_form, 'book': book})

    def post(self, request, slug):
        book = get_object_or_404(Book, slug__iexact=slug)
        bound_form = CreateBookForm(request.POST, instance=book)
        if bound_form.is_valid():
            update_book = bound_form.save()
            return redirect(update_book.get_absolute_url())
        return render(request, 'book/book_detail.html', {'form': bound_form, 'book': book})


class DeleteBook(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request, slug):
        book = get_object_or_404(Book, slug__iexact=slug)
        return render(request, 'book/delete_book.html', {'book': book})

    def post(self, request, slug):
        book = get_object_or_404(Book, slug__iexact=slug)
        book.delete()
        return redirect(reverse('book_list'))


class Register(RegisterOrLoginMixin, CreateView):
    form_class = RegistrationForm
    template_name = 'book/register.html'
    register_or_login_form = 'registration_form'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('book_list')


class Login(RegisterOrLoginMixin, LoginView):
    form_class = LoginForm
    template_name = 'book/login.html'
    register_or_login_form = 'login_form'


def logout_user(request):
    logout(request)
    return redirect('book_list')


def profile(request):
    return render(request, 'book/profile.html')
