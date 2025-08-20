from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, PostViewSet, CommentViewSet

# -------------------
# Router for Post & Comment ViewSets
# -------------------
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'comments', CommentViewSet, basename='comments')

# -------------------
# URL Patterns
# -------------------
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', RegisterView.as_view(), name='profile'),  # placeholder for profile
    path('', include(router.urls)),  # Include posts & comments routes
]
