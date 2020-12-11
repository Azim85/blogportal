from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

def index(request):
    posts = Post.objects.order_by('-post_added')
    context = {'posts':posts}
    return render(request, 'main/index.html', context)


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.author = request.user
            user.save()
            return redirect('main:index')
    form = PostForm()
    return render(request, 'main/post_create.html', {'form':form})