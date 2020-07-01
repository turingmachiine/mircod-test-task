from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Author, Book, Order
from api.tasks import send_email


class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True)
    books_count = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ["id", "full_name", "books", "books_count"]

    def get_books_count(self, obj):
        return obj.books.count()


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(read_only=True)

    def create(self, validated_data):
        order = Order.objects.create(
            customer=self.context["request"].user, **validated_data
        )
        for user in User.objects.filter(is_superuser=True):
            send_email.delay(
                "New Order",
                settings.DEFAULT_FROM_EMAIL,
                user.email,
                "mail.html",
                args=dict(
                    order_book=order.book.title, order_customer=order.customer.username
                ),
            )
        return order

    class Meta:
        model = Order
        fields = ("book", "cust_phone", "customer")
