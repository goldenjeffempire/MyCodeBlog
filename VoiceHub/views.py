from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

# View to list all posts
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'VoiceHub/post_list.html', {'posts': posts})

# View to create a new post
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'VoiceHub/create_post.html', {'form': form})

# View to display details of a specific post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'VoiceHub/post_detail.html', {'post': post})
