from django.shortcuts import render
from appNewest.models import Book

# Create your views here.

def index(request):
    return render(request,'appNewes/index.html')

def bookThis(request):
    book_list = Book.objects.order_by('bookTitle')
    book_dict = {'books':book_list}
    return render (request, 'appNewest/index.html', context=book_dict)