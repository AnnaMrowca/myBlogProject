from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post
from blog.forms import PostForm



def home(request):
    #tworzymy queryset, twoerzony dzięki danym z bazy danych
    posts = Post.objects.all().order_by('-date')
    #przekazujemy queryset do templatki
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


def detail(request, postId):
    post = get_object_or_404(Post, pk=postId)
    return render(request, 'detail.html', {'post': post})










