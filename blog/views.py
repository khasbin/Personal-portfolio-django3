from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blog
# Create your views here.

def all_blogs(request):
    counting = Blog.objects.all()
    context = Blog.objects.order_by('-date')[:4]
    return render(request, 'blog/blog.html',{'contexts':context, 'counting':counting})


def details(request,blog_id):
    thing = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'blog/detail.html',{'thing':thing})

