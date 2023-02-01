from django.shortcuts import render

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .models import Book,Author

from .forms import BookForm

# Create your views here.

def home_page(request):
    return render(request,'library_home.html')

def book_page(request):
    return render(request,'library_book.html')

def book_detail_page(request,book_num):
    context = {
        'book_num':book_num,
    }
    return render(request,'library_book_detail.html',context)



#  book list page
class BookList(ListView):
    model = Book
    template_name = "booklist.html"

#  author list page
class AuthorList(ListView):
    model = Author
    template_name = "authorlist.html"

# book create page
class BookCreate (CreateView):
    model = Book
    template_name = "createbook.html"
    fields = "__all__"
    success_url = '/createbook/'

# book detail page
class BookDetail (DetailView):
    model = Book
    template_name = "bookdetail.html"

# update book page
class BookUpdate (UpdateView):
    model = Book
    template_name = "bookupdate.html"
    fields = ["Title","Author"]
    success_url = '/'

# book delete page
class BookDelete(DeleteView):
    model = Book
    template_name = "bookdelete.html"
    success_url = '/'