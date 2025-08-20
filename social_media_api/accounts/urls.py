from django.urls import path
from .views import RegisterView, LoginView, FollowUserView, UserListView  # assuming views are already created

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path("users/", UserListView.as_view(), name="user-list"),
    #path('profile/', RegisterView.as_view(), name='profile'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),    # placeholder; can extend later
    path('unfollow/<int:user_id>/', FollowUserView.as_view(), name='unfollow-user'),
]
