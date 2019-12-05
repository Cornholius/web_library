from django.db import models


class Library(models.Model):

    author = models.CharField(max_length=120, null=False)
    book_name = models.CharField(max_length=120, null=False)
    description = models.CharField(max_length=1200, null=False)

    # def __str__(self):
    #     return str(self.author) + "\n" + str(self.book_name) + "\n" + str(self.description)

    def gfd(self):
        return self.author, self.book_name, self.description


