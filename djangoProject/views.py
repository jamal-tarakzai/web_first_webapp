from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'index.html', {'key1': 'i am coming from python code'})


def results(request):
    article = request.GET['article']

    return render(request, 'results.html', {'article': article})
