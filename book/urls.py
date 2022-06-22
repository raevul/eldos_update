from django.urls import path

from .views import *

urlpatterns = [
    path('', book_list, name='book_list'),
    path('sing-up/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', logout_user, name='logout'),
    path('<str:slug>/', books_filter, name='books_filter'),
    path('book/create/', CreateBook.as_view(), name='create_book'),
    path('book/<str:slug>/update/', UpdateBook.as_view(), name='update_book'),
    path('book/<str:slug>/delete/', DeleteBook.as_view(), name='delete_book'),
    path('book/<str:slug>/read/', read_book, name='read_book'),
    path('book/<str:slug>/', book_detail, name='book_detail'),
    path('author/<int:pk>/', author_detail, name='author_detail'),
]
