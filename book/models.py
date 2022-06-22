from django.db import models
from django.shortcuts import reverse


class Book(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='books')
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='books')
    genre = models.ManyToManyField('Genre', related_name='books')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title', )

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('update_book', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('delete_book', kwargs={'slug': self.slug})


class Author(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    image = models.ImageField(blank=True, null=True, upload_to='authors')

    def __str__(self):
        return f'{self.name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('author_detail', kwargs={'pk': self.pk})


class Genre(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('books_filter', kwargs={'slug': self.slug})
