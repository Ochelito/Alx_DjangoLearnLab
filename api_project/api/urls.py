from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import BookViewSet, BookList
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),  # This includes all routes registered with the router
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]