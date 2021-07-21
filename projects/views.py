from django.shortcuts import render
from .models import Project

def homepage(response):
    instance = Project.objects.all()
    return render( response, 'projects/one.html', {'projects' : instance})