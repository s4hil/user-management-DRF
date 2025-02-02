from django.urls import path
from .views import RegisterUserView, LoginUserView, LoginSuperUserView, ManageUsersView, UserDetailView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='user-register'),
    path('login/', LoginUserView.as_view(), name='user-login'),
    path('superuser-login/', LoginSuperUserView.as_view(), name='superuser-login'),
    path('manage-users/', ManageUsersView.as_view(), name='manage-users'),
    path('manage-users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]
