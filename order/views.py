from django.shortcuts import render, redirect

from book.models import Book
from .forms import OrderForm


def order(request, slug):
    book = Book.objects.get(slug=slug)
    order_form = OrderForm(request.POST)
    if order_form.is_valid():
        order_form.save()
        return redirect(book.get_absolute_url())
    return render(request, 'order/order.html', {'order_form': order_form, 'book': book})
