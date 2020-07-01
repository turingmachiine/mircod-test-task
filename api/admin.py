from django.contrib import admin

# Register your models here.
from api.models import Author, Book, Order

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Order)
