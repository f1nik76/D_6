from django.urls import path
from news.views import ListNews, NewsDetail

urlpatterns = [
    path('news/', ListNews.as_view()),
    path('news/<pk>', NewsDetail.as_view()),
]