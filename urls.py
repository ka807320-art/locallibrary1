from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("book/<int:pk>/", views.book_detail, name="book-detail"),
    path("author/<int:pk>/", views.author_detail, name="author-detail"),
    path("language/<int:pk>/", views.language_detail, name="language-detail"),
]
