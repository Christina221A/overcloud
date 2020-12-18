from django.shortcuts import render
from webapp.views import index


def homepage(request):
    return render(request, 'webapp/index.html')
