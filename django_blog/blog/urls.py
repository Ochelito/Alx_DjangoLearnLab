from django.urls import path
from .views import UserRegisterView, ProfileView, HomeView, CustomLogoutView, CustomLoginView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView 

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),  
    path('profile/', ProfileView.as_view(), name='profile'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]

