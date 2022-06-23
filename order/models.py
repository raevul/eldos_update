from django.db import models
from django.shortcuts import reverse
from book.models import Book


class Order(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='orders')
    phone = models.CharField(max_length=13)
    address = models.TextField()
    city = models.CharField(max_length=100)
    email = models.EmailField()

    # def get_absolute_url(self):
    #     return reverse('order', kwargs={'slug': self.Book.slug})

    def __str__(self):
        return f'{self.email}'
