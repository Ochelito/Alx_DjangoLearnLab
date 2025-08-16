from django.urls import path
from .views import UserRegisterView, ProfileView, HomeView  
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  
    path('profile/', ProfileView.as_view(), name='profile'),
]

