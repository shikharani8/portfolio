from django.shortcuts import render, get_object_or_404
from .models import BlogModel

# Create your views here.
def home(request):
    #blogs = BlogModel.objects.order_by('-date')[:5]
    blogs = BlogModel.objects.order_by('-date')
    return render(request, 'blog/home.html', {'blogs': blogs})


def details(request, blog_id):
    blog = get_object_or_404(BlogModel, pk= blog_id)
    return render(request, 'blog/details.html', {'blog': blog})
