from django.shortcuts import render
from .models import NewsArticle

# Create your views here.

def news_list(request):
    articles = NewsArticle.objects.all()
    print(articles)
    return render(request, 'core/home.html', {'articles':articles})