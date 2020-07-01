from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class Author(models.Model):
    full_name = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ["author"]


class Order(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    cust_phone = models.CharField(max_length=12)
    comment = models.TextField(default="")
    date_ordered = models.DateTimeField(default=timezone.now)
