from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

# Views
from collection_books.categories.api.views import CategoryViewSet
from collection_books.users.api.views import UserViewSet
from collection_books.books.api.views import BookViewSet
from collection_books.authors.api.views import AuthorViewSet
from collection_books.narrators.api.views import NarratorViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("categories", CategoryViewSet)
router.register("books", BookViewSet)
router.register("authors", AuthorViewSet)
router.register("narrators", NarratorViewSet)


app_name = "api"
urlpatterns = router.urls
