from django.urls import path
from . import views

urlpatterns = [
    path('student/', views. QueryView.as_view()),
    path('books/', views.BookView.as_view())
]