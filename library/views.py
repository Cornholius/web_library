from django.shortcuts import render
from django.views.generic import View
from .forms import UserForm
from .models import Library
from django.db.models import Q


class BookView(View):

    def get(self, request):
        return render(request, "home/index.html", {"search_recuest": UserForm})

    def post(self, request):
        name_from_form = request.POST.get("name")
        name = str(name_from_form).capitalize()
        books = Library.objects.filter(Q(author__contains=name) | Q(book_name__contains=name))
        if not books:
            return render(request, "home/index.html", {"search_recuest": UserForm,
                                                       "book_not_found": "Автор или Книга не найдены"})
        else:
            return render(request, 'home/index.html', {"search_recuest": UserForm, 'books': books})
