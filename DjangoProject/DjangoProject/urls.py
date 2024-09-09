from django.contrib import admin
from django.urls import path

from FirstDjangoApp.views import ProjectDetails

urlpatterns = [
    path('admin/', admin.site.urls),
]