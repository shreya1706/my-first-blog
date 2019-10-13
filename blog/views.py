from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'blog/post_list.html', context)
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post' : post
    }
    return render(request, 'blog/post_detail.html', context)
