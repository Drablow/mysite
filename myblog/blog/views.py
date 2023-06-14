from django.shortcuts import render
from django.views.generic.base import View
from .models import Post


class PostView(View):
    """ Вывод записей """

    def get(self, request):
        posts = Post.objects.all()
        context = {
            'posts': posts
        }
        return render(request, 'blog/home.html', context=context)


class AboutView(View):
    """ Вывод информации о проекте"""
    def get(self, request):
        context = {
            'title': 'О проекте VL Blog'
        }
        return render(request, 'blog/about.html', context)


