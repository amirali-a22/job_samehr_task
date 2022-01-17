from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class Index(View):
    # pass
    def get(self, request):
        return HttpResponse('<h1>this is index page</h1>')
