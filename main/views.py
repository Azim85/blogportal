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

def post_edit(request, post_id):
    from datetime import datetime
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            user = form.save(commit=False)
            user.post_added = datetime.now()
            user.author = request.user
            user.save()
            return redirect('profile')
    form = PostForm(instance=post)
    return render(request, 'main/post_edit.html', {'post':post, 'form':form, 'id':post_id})

def post_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    if request.GET.get('from') == 'profile':
        return redirect('profile')
    return redirect('main:index')