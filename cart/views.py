from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST


from book.models import Book
from .helpers import Cart
from .forms import CartAddBookForm


@require_POST
def cart_add(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    form = CartAddBookForm(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        cart.add_or_update(
            book=book,
            quantity=cleaned_data['quantity'],
            update_quantity=cleaned_data['update']
        )
    return redirect('cart:cart_detail')


def cart_remove(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    cart.remove(book)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart_detail.html', {})
