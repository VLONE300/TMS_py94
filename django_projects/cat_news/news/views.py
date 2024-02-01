from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import News


# Create your views here.
class NewsIndexView(View):

    def get(self, request):
        sorting_param = request.GET.get('name_sorting', '')
        priority_sorting = request.GET.get('priority_sorting', '')
        news = News.objects.order_by(f'{priority_sorting}{sorting_param}' or 'pk')
        return render(request, 'news/index.html', context={"news": news})
