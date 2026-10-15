from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.utils.dateparse import parse_date


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
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


#
class LatestPostView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10

    def get_queryset(self):
        # 1. Start with the default queryset
        queryset = super().get_queryset()

        # 2. Check for the 'date' filter in the URL
        date_str = self.request.GET.get('date')
        if date_str:
            selected_date = parse_date(date_str)
            if selected_date:
                # This strictly filters to ONLY the selected date
                queryset = queryset.filter(date_posted__date=selected_date)

        # 3. Check for the 'filter=latest' parameter (from your other button)
        filter_type = self.request.GET.get('filter')

        if filter_type == 'latest':
            return queryset.order_by('-date_posted')

            # You can add other filters here later (e.g., if filter_type == 'popular')
        return queryset.order_by('-date_posted')