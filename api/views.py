from rest_framework import viewsets
from rest_framework import mixins
from django.shortcuts import render

from api.models import Author, Book, Order
from api.permissions import AuthorCustomPermission
from api.serializers import AuthorSerializer, BookSerializer, OrderSerializer


class AuthorViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class OrderViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
