from django.urls import path
from .views import news_list, news_detail

urlpatterns = [
    path('news/', news_list, name='news_list'),
    path('news_detail/<int:news_id>/', news_detail, name='news_detail'),
]
