from django.urls import path
from . import views
urlpatterns =[
    path('', views.home, name='home'),
    path('book/',views.book,name='book'),
    path('book_details/<id>/<tag>/',views.book_details,name='book_details'),
]