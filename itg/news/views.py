from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

def get_all_news(request):
    return render(request, 'news/catalog.html')

def get_news_by_id(request, news_id):
    return HttpResponse(f"Новость номер {news_id}")

def main(request):
    return render(request, 'base.html')
