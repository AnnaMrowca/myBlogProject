from django.shortcuts import render, redirect
from blog.models import Post
from blog.forms import PostForm
from django.contrib import messages


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def create(request):
    if request.method == 'GET':
        return render(request, 'create.html', {'form': PostForm()})
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Something went wrong'
            return render(request, 'create.html', {'form': PostForm(), 'error': error})










