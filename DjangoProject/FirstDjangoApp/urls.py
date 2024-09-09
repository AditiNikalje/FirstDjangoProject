from django.urls import path
from . import views

urlpatterns = [
    path('getProjectDetails/', views.ProjectDetails, name='Get UIReport Configuration'), 
]