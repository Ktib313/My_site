from django.shortcuts import render

# Create your views here.
def blog_home(request):
    return render(request, 'blog/home.html')

def blog_posts(request):
    return render(request, 'blog/posts.html')

def blog_post_detail(request, slug):
    return render(request, 'blog/post_detail.html', {'slug': slug})