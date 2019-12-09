from django.shortcuts import render
from django.views.generic import View
from .forms import UserForm, AddBookForm, DeleteBookForm
from .models import Library
from django.db.models import Q


class BookView(View):

    def get(self, request):
        return render(request, "home/index.html", {"search_recuest": UserForm})

    def post(self, request):
        name_from_form = request.POST.get("search_field")
        name = str(name_from_form).capitalize()
        books = Library.objects.filter(Q(author__contains=name) | Q(book_name__contains=name))
        if not books:
            return render(request, "home/index.html", {"search_recuest": UserForm,
                                                       "book_not_found": "Автор или Книга не найдены"})
        else:
            return render(request, 'home/index.html', {"search_recuest": UserForm, 'books': books})


class AddBookView(View):

    def get(self, request):
        return render(request, 'addbook/index.html', {"search_recuest": UserForm, 'form': AddBookForm})

    def post(self, request):
        author_field = str(request.POST.get("author")).capitalize()
        book_name_field = str(request.POST.get("book_name")).capitalize()
        description_field = str(request.POST.get("description")).capitalize()
        Library.objects.create(author=author_field, book_name=book_name_field, description=description_field)
        return render(request, 'addbook/index.html', {'form': AddBookForm, 'book_added': "книга успешно добавлена"})


class DeleteBookView(View):

    def get(self, request):
        return render(request, 'deletebook/index.html', {'form': DeleteBookForm})

    def post(self, request):
        author_field = request.POST.get("author")
        book_name_field = request.POST.get("book_name")
        Library.objects.filter(author=author_field, book_name=book_name_field).delete()
        return render(request, 'deletebook/index.html', {'form': DeleteBookForm, 'book_deleted': "книга успешно удалена"})


class AllBooksView(View):

    def get(self, request):
        books = Library.objects.all()
        return render(request, 'allbooks/index.html', {'books': books})
