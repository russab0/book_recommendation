from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    first_name = models.CharField('First Name', max_length=30)
    middle_name = models.CharField('Middle Name', max_length=30, null=True, blank=True)
    last_name = models.CharField('Last Name', max_length=30)


class Book(models.Model):
    title = models.CharField('Title', max_length=50)
    authors = models.ManyToManyField(Author)
    description = models.TextField('Description', max_length=500)


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField('Content', max_length=500)
    rating = models.IntegerField('Rating')
