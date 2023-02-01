from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book,Author


# Create your views here.

def home(request):
    return render(request,'home.html')

def book(request):
    books=Book.objects.all()
    return render(request,'books.html',{'books':books})

def bookcreate(request):
    books=Book.objects.get(id=book_id)
    return render(request,'addbook.html',)

def book_delete(request,book_id):
    books=Book.objects.get(id=book_id)
    books.delete()
    return redirect('library:book')
   
def book_edit(request,book_id):
    books=Book.objects.get(id=book_id)
    return render(request,'book_edit.html',{'books':books})

def update(request,book_id):
    updatebook=Book.objects.get(id=book_id)
    authid=updatebook.Author_id
    updateauthor=Author.objects.get(id=authid)
    print(authid)
    if request.method =='POST':
        title=request.POST['T_title']
        author=request.POST['A_author']
        summary=request.POST['S_summary']
        date=request.POST['Pdate']
        updatebook.Title=title
        updateauthor.Name=author
        updatebook.Summary=summary
        updatebook.Date=date
        updatebook.save()
        updateauthor.save()
        books=Book.objects.all()

        return render(request,'books.html',{'books':books})

def add_book(request):
    return render(request,'addbook.html')

def add_submit(request): 
    if request.method =='POST':
        title=request.POST.get('t_title')
        print(title)
        author_name=request.POST.get('a_author')
        author, created=Author.objects.get_or_create(Name=author_name)
        summary=request.POST.get('s_summary')
        date=request.POST.get('d_date')
        book=Book(Title=title,Author=author,Summary=summary,Published_date=date)
        book.save()
        books=Book.objects.all()

        return render(request,'books.html',{'books':books})
    

def author_view(request):
    authors=Author.objects.all()
    return render(request,'author_view.html',{'authors':authors})

def book_details(request,book_id):
    books=Book.objects.get(id=book_id)
    return render(request,'books_detail.html',{'books':books})



