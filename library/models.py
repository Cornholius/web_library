from django.db import models


class Library(models.Model):

    author = models.CharField(max_length=120, null=False)
    book_name = models.CharField(max_length=120, null=False)
    description = models.CharField(max_length=1200, null=False)
