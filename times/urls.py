from django.urls import path

from times.views import (
    TimeCreateView,
    TimeDetailView,
)


app_name = 'times'

urlpatterns = [
    path('', TimeCreateView.as_view(), name='create'),
    path('<int:id>/', TimeDetailView.as_view(), name='detail'),
]
