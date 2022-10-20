from django.urls import path

from times.views import (
    TimeCreateView,
)


app_name = 'times'

urlpatterns = [
    path('', TimeCreateView.as_view(), name='create')
]
