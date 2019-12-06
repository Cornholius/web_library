from django.shortcuts import render
from django.views import View
from .forms import UserForm, UserForm2
from django.http import HttpResponse
from .models import Library
import sqlite3

def all_books(request):
    books = Library
    return render(request, "home/2.html", {'books': books})


def find_book(request):
    if request.method == "POST":
        name_from_form = request.POST.get("name")
        name = str(name_from_form).capitalize()
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()
        sql_recuest = f"SELECT author, book_name, description " \
                      f"FROM library_library " \
                      f"WHERE book_name like '%{name}%' " \
                      f"OR author like '%{name}%'"
        cursor.execute(sql_recuest)
        result = cursor.fetchall()  #   one - одна запись.  all - все записи
        print(result)
        print(result[0])
        try:
            return render(request, "home/2.html", {"search_recuest": UserForm,
                                                       "author": result[0],
                                                       "bookname": result[1],
                                                       "description": result[2]})
        except:
            return render(request, "home/index.html", {"search_recuest": UserForm,
                                                       "author": "Автор или Книга не найдены"})

    else:
        return render(request, "home/index.html", {"search_recuest": UserForm})


class HomeView(View):

    def get(self, request):
        return render(request, 'home/index.html')
