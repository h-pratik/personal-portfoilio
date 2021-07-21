from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(response):
    instance = Blog.objects.all()
    return render(response, "one.html", {'returned' : instance})

def details(response, id):
    id = get_object_or_404(Blog, pk = id)
    return render(response, "details.html", {"blog_id":id})
