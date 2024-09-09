from django.shortcuts import render

from FirstDjangoApp.models import Project

# Create your views here.
class ProjectDetails():

    def getProjectDetails():
        project_details = Project.objects.all()
        return project_details