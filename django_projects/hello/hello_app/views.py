from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


# Create your views here.
class HelloView(View):
    def get(self, request):
        string = "hello"
        return render(request, 'hello/hello.html', context={'string': string})


class HelloWorldView(View):
    def get(self, request):
        string = "hello world"
        return render(request, 'hello/hello.html', context={'string': string})
