from django.urls import path
from . import views

app_name = 'sample' 

urlpatterns = [
    path('index/', views.index, name='index'),
    path('list/', views.SampleList.as_view(), name='list'),
    path('', views.YoutubeSearchView.as_view(), name='youtube_search'),
    ]