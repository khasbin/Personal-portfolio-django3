from django.shortcuts import render
from django.http import HttpResponse
from .models import blog
# Create your views here.

def all_blogs(request):
    context = blog.objects.order_by('-date')[:3]
    return render(request, 'blog/blog.html',{'contexts':context})
