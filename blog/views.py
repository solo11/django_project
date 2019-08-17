from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def post_list(request) :
    posts_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    page  = request.GET.get('page',1)

    paginator = Paginator(posts_list,5)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        
    return render (request,'blog/post_list.html',{'posts':posts})

def post_detail(request,pk):
    post = get_object_or_404(Post , pk = pk)
    return render(request, 'blog/post_detail.html',{'post':post})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk = post.pk)

    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})

def post_edit (request, pk):
    post = get_object_or_404(Post, pk = pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk = post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html',{'form':form})