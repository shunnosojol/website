from django.shortcuts import render
from .models import Resume ,Post
from django.views.generic import ListView

from forms import ContactMe
# Create your views here.
def home(request):
    return render(request, 'resume/home.html')

def about(request):
    resume = Resume.objects.get(pk = 1)
    return render(request, 'resume/about.html',{'resume':resume})


#def blog(request):
 #   context = {
  #          'posts'  : Post.objects.all()
   #     }
    return render(request, 'resume/blog.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'resume/blog.html'
    context_object_name = 'posts'
    ordering = ['-date']

def form(request):
    form = ContactMe()
    return render(request, 'resume/form.html',{'form' = form})