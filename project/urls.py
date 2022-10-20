from django.urls import path

from project.views import (
    ProjectCreateView,
    ProjectDetailView
)


app_name = 'project'

urlpatterns = [
    path('', ProjectCreateView.as_view(), name='create'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='detail')
]
