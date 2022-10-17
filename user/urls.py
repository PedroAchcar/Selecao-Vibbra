from django.urls import path

from user.views import (
    UserCreateView,
    UserDetailView,
)


app_name = 'user'

urlpatterns = [
    path('', UserCreateView.as_view(), name='create'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail')
]
