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
from library.views import HomeView

def get_book_by_id(request, book_id):
    name = Library.objects.get(id=book_id,)
    author = name.author
    bookname = name.book_name
    desc = name.description
    return HttpResponse(f'{author} '
                        f'{bookname} '
                        f'{desc}')


urlpatterns = [
        path('', HomeView.as_view()),
        path('<int:book_id>', get_book_by_id)
]