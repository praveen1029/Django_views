from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page,name='home'),
    path('book/',views.book_page,name='book'),
    path('book/<int:book_num>/details/',views.book_detail_page,name='book_detail'),
    path('booklist/',views.BookList.as_view(),name='booklist'),
    path('authorlist/',views.AuthorList.as_view(),name='authorlist'),
    path('createbook/',views.BookCreate.as_view(),name='createbook'),
    path('<pk>/',views.BookDetail.as_view(),name='bookdetail'),
    path('update/<pk>/',views.BookUpdate.as_view(),name='bookupdate'),
    path('delete/<pk>/',views.BookDelete.as_view(),name='bookdelete'),
]