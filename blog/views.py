from typing import Optional
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# posts = [
#     {
#         'author': 'amirHossein',
#         'title': 'post 1',
#         'content': 'first post content',
#         'data': '28/2/1413',
#     },
#     {
#         'author': 'Mahdi',
#         'title': 'post 2',
#         'content': 'second post content',
#         'data': '2/12/1409',
#     }
# ]


# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model =Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView): 
    model = Post
    fields= ['title', 'content']
    success_url = reverse_lazy('blog-home')
    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
    model = Post
    fields= ['title', 'content']
    success_url = reverse_lazy('blog-home')
    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)


    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        else:
            return False

 

def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
