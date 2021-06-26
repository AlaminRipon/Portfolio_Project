from django.shortcuts import render, get_object_or_404
from .models import Blog

def blogs(request):
  context = {
    'blogs': Blog.objects
  }
  return render(request, 'blogs/blog.html', context)

def detail(request, blog_id):

  detail_blog =  get_object_or_404(Blog, pk=blog_id)

  return render(request, 'blogs/detail.html', {'blog':detail_blog})
