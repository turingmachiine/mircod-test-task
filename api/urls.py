from rest_framework.routers import DefaultRouter

from api.views import AuthorViewSet, BookViewSet, OrderViewSet

router = DefaultRouter()
router.register(r"authors", AuthorViewSet, basename="api-authors")
router.register(r"books", BookViewSet, basename="api-books")
router.register(r"orders", OrderViewSet, basename="api-orders")
urlpatterns = router.urls
