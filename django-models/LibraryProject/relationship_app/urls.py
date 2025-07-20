from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from . import views
#from .views import list_books, LibraryDetailView, register

urlpatterns = [
    path('', views.list_books, name='list_books'),
    path('relationship_app/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register')
]
