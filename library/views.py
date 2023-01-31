from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request,'home.html')

def book(request):
    return render(request,'books.html')

def book_details(request,id,tag):
    return render(request,'books_detail.html')