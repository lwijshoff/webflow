from django.urls import path
from . import views

app_name = 'lunch'

urlpatterns = [
    path('', views.booking, name='lunch_booking'),
    path('book/', views.book_ajax, name='lunch_book'),
]
