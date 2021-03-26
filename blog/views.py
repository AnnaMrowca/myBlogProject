from django.shortcuts import render
from blog.models import Post
from blog.forms import PostForm

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def create(request):
    return render(request, 'create.html', {'form':PostForm()})
