from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator
import random
# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('-date')
    paginator = Paginator(posts, 2)
    paginator.orphans = 1
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_posts': page_posts})
def post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request,'post.html', {'post': post})
def about(request):
    return render(request, 'about.html')
def Random(request):
    #obj_number = Post.objects.count()
    #rand_post = Post.objects.get(id = random.randint(1,obj_number))
    items = list(Post.objects.all())
    rand_post = random.choice(items)
    return render(request, 'post.html', {'post': rand_post})
