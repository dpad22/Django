from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('authors', views.authors),
    path('book/<book_id>', views.view_book),
    path('author/<author_id>', views.view_author),
    path('add_book', views.add_book),
    path('createAuthor', views.createAuthor),
    path('add_author/<book_id>', views.add_author),
    path('join_book/<author_id>',views.join_book)

]