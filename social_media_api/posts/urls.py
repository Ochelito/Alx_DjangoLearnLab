from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'comments', CommentViewSet, basename='comments')

# Include the router URLs in urlpatterns
urlpatterns = [
    path('', include(router.urls)),
]
