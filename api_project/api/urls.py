from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as auth_views

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book') # Register the BookViewSet with the router

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls())),  # Include the router URLs
    path('api-token-auth/', auth_views.obtain_auth_token, name='api_token_auth'), # URL for obtaining auth token
]


# This file is used to define the API URLs for the application.
# It includes the URL for the BookList which lists all books.