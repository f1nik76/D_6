from django.shortcuts import render
from django.views.generic import ListView, DetailView

from news.models import News


# Create your views here.


class ListNews(ListView):
    model = News
    ordering = 'date_pub'
    template_name = 'news/news.html'
    context_object_name = 'news'


class NewsDetail(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news'