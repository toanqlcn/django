from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('authors/', views.author_list, name='author_list'),
    path('authors/<int:pk>/', views.author_detail, name='author_detail'),
    path('authors/create/', views.author_create, name='author_create'),
    path('authors/edit/<int:pk>/', views.author_edit, name='author_edit'),
    path('authors/delete/<int:pk>/', views.author_delete, name='author_delete'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('books/create/', views.book_create, name='book_create'),
    path('books/edit/<int:pk>/', views.book_edit, name='book_edit'),
]
