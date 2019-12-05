from django.shortcuts import render
from django.views import View
from .forms import UserForm, UserForm2
from django.http import HttpResponse
from .models import Library
import sqlite3

"""
в index мы получаем в переменную из строки поиска.
надо реализовать поиск в базе по значению из переменной
вывести полностью всю книгу на страницу"""


def find_book(request):
    if request.method == "POST":
        name = request.POST.get("name")
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()
        sql_recuest = f"SELECT author, book_name, description FROM library_library WHERE book_name = '{name}'"
        cursor.execute(sql_recuest)
        result = cursor.fetchone()
        # try:
        #     return HttpResponse(result[0:])
        #
        # except:
        #     return HttpResponse("книга не найдена")
        return render(request, "home/index.html", {"author": result[0], "bookname": result[1], "description": result[2]})

    else:
        userform = UserForm()
        return render(request, "home/index.html", {"form": userform})


class HomeView(View):

    def get(self, request):
        return render(request, 'home/index.html')

    def find_book(self):
        if request.method == "POST":
            name = request.POST.get("name")
            connection = sqlite3.connect('db.sqlite3')
            cursor = connection.cursor()
            sql_recuest = f"SELECT author, book_name, description FROM library_library WHERE book_name = '{name}'"
            cursor.execute(sql_recuest)
            result = cursor.fetchone()
            try:
                return HttpResponse(result[0:])

            except:
                return HttpResponse("книга не найдена")
        else:
            userform = UserForm()
            return render(request, "home/index.html", {"form": userform})


# def index(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         # age = request.POST.get("age")     # получение значения поля age
#         return HttpResponse("<h2>Hello, {0}</h2>".format(name))
#     else:
#         userform = UserForm()
#         return render(request, "home/index.html", {"form": userform})