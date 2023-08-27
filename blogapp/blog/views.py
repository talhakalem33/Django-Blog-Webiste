from django.shortcuts import render
from blog.models import Blog

# Create your views here.
def index(request):
    context = {
        "blogs" : Blog.objects.filter(isactive = True)
    }

    return render(request, "blog/index.html")