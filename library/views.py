from django.shortcuts import render
from django.views import View
from .forms import UserForm
from django.http import HttpResponse
from .models import Library

"""
в index мы получаем в переменную из строки поиска.
надо реализовать поиск в базе по значению из переменной
вывести полностью всю книгу на страницу"""


def index(request):
    if request.method == "POST":
        ololo = request.POST.get("name")
        print(ololo)


class HomeView(View):

    def get(self, request):
        return render(request, 'home/index.html')




# def index(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         # age = request.POST.get("age")     # получение значения поля age
#         return HttpResponse("<h2>Hello, {0}</h2>".format(name))
#     else:
#         userform = UserForm()
#         return render(request, "home/index.html", {"form": userform})