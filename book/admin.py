from django.contrib import admin

from .models import *


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}


class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Author)
admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Comment)
