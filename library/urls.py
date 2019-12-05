"""web_library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.http import HttpResponse
from .models import Library
from library.views import HomeView, find_book
import sqlite3

def get_book_by_id(request, book_id):
    name = Library.objects.get(id=book_id,)
    author = name.author
    bookname = name.book_name
    desc = name.description
    return HttpResponse(f'{author} {bookname} {desc}')

# def find_book():
#     connection = sqlite3.connect('db.sqlite3')
#     cursor = connection.cursor()
#
#     cursor.execute("""
#         SELECT author, book_name, description
#         FROM library_library
#         WHERE book_name = 'qwerty2'
#         """)
#     return HttpResponse(cursor.fetchone())
#     print(cursor.fetchone())



urlpatterns = [
        path('', find_book),
        path('z/', find_book),
        path('<int:book_id>', get_book_by_id)
]
