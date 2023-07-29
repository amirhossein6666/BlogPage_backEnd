from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

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


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
