from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.db.models import Q
from project.decorators import anonymous_required


# def index(request):
#     posts = Post.objects.order_by('-post_added')
#     paginator = Paginator(posts, 2)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
    
#     context = {'posts':posts, 'page_obj':page_obj}
#     return render(request, 'main/index.html', context)
class IndexView(ListView):
    model=Post
    template_name='main/index.html'
    paginate_by = 2
    ordering = ['-post_added']
    context_object_name = 'posts'
    

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.author = request.user
            user.save()
            return redirect('main:index')
    form = PostForm()
    return render(request, 'main/post_create.html', {'form':form})

@login_required
def post_edit(request, post_id):
    from datetime import datetime
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            user = form.save(commit=False)
            user.post_added = datetime.now()
            user.author = request.user
            user.save()
            return redirect('main:index')
    form = PostForm(instance=post)
    return render(request, 'main/post_edit.html', {'post':post, 'form':form, 'id':post_id})

@login_required
def post_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    if request.GET.get('from') == 'profile':
        return redirect('profile')
    return redirect('main:index')


def post_more(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        return render(request, 'main/more.html', {'post':post, 'id':post_id})
    except :
        return redirect('main:index')
    
def post_all(request, user_id):
    user = User.objects.get(id=user_id)
    posts = user.post_set.all().order_by('-post_added')
    return render(request, 'main/post_all.html', {'posts':posts})

 
class SearchResaultView(ListView):
    model = Post
    template_name = 'main/search.html'

    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        
        return object_list
