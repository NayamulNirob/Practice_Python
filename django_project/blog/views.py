import datetime

from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# posts=[
#     {'author':'John dou',
#      'title' :'John dou\'s blog',
#      'content':'John dou first blog.........',
#      'date_posted':datetime.date.today()
#      },
#      {'author':'Steven byard',
#      'title' :'Steven byard\'s blog',
#      'content':'Steven byard first blog.........',
#      'date_posted':datetime.date.today()
#      },
#     {'author':'Bob hone',
#      'title' :'Bob hone\'s blog',
#      'content':'Bob hone first blog.........',
#      'date_posted':datetime.date.today()
#      }
# ]

# Create your views here.
def home(request):
    context = {
        # 'posts': posts
        'posts': Post.objects.all(),
    }
    return render(request,'blog/home.html',context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

def about(request):
    return render(request,'blog/about.html',{'title':'About'})