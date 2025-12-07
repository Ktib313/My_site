from django.shortcuts import render
from datetime import date


all_posts = [
    {
        'slug': 'getting-started-with-django',
        'title': 'Getting Started with Django',
        'excerpt': 'An introduction to Django framework and how to get started.',
        'date': date(2024, 1, 15),
        'content': 'Full content of the Getting Started with Django post...',
        'image_url': 'mountains.jpg',
        'author':  'Modou'
    },
    {
        'slug': 'advanced-django-models',
        'title': 'Advanced Django Models',
        'excerpt': 'Diving deeper into Django models and their capabilities.',
        'date': date(2024, 2, 20),
        'content': 'Full content of the Advanced Django Models post...',
        'image_url': 'max.png',
        'author':  'Modou'
    },
    {
        'slug': 'deploying-django-applications',
        'title': 'Deploying Django Applications',
        'excerpt': 'Best practices for deploying Django applications to production.',
        'date': date(2024, 3, 10),
        'content': 'Full content of the Deploying Django Applications post...',
        'image_url': 'woods.jpg',
        'author':  'Modou'
    },
]
# Create your views here.
def blog_home(request):
    sorted_posts = sorted(
        all_posts,
        key=lambda post: post['date'],
        reverse=True
    )   
    latest_posts = sorted_posts[:3]
    return render(request, 'blog/home.html', {'posts': latest_posts})

def blog_posts(request):
    return render(request, 'blog/all-posts.html', {'posts': all_posts})

def blog_post_detail(request, slug):
    new_post = next((post for post in all_posts if post['slug'] == slug), None) 
    return render(request, 'blog/post-detail.html', {'post': new_post})