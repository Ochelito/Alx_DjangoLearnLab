from django.urls import path
from .views import RegisterView, LoginView  # assuming views are already created

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', RegisterView.as_view(), name='profile'),  # placeholder; can extend later
]
