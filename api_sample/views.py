from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, View
from .models import Sample
from django.db.models import Q
from . import get_data_api
# Create your views here.
def index(request):
    return HttpResponse("Hello API APP")

class SampleList(ListView):
    model = Sample
    template_name = 'list.html'
    context_object_name = 'sample_list'

    def get_queryset(self):
        q_w = self.request.GET.get('query')
        if q_w:
            queryset = Sample.objects.filter(Q(title__icontains=q_w) | Q(contributor__icontains=q_w))
        else:
            pass
        return queryset

class YoutubeSearchView(View):

    def get(self, request, *args, **kwargs):
        if 'word' in request.GET:
            keyword = request.GET['word']
            youtube_df = get_data_api.youtube_search(keyword)

            context = {
                    "word":keyword,
                    'df':youtube_df.to_html(),
            }
            print(context)
            return  render(request, 'result.html', context)

        return render(request, "search.html")


