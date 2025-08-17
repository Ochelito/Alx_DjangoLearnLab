from django.urls import path
from .views import UserRegisterView, ProfileView, HomeView, CustomLogoutView, CustomLoginView 

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),  
    path('profile/', ProfileView.as_view(), name='profile'),
]

