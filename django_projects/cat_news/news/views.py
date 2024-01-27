from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import News


# Create your views here.
class NewsIndexView(View):
    news = News.objects.all().order_by('-date')

    def get(self, request):
        return render(request, 'news/index.html', context={"news": self.news})
