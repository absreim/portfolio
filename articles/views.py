from django.shortcuts import render

from .models import Article

def index(request):
    articles = Article.objects.order_by('-date')
    context = {
        'articles': articles
    }
    return render(request, 'articles/list.html', context)

def single(request, article_id):
    article = Article.objects.get(pk=article_id)
    context = {
        'article': article
    }
    return render(request, 'articles/single.html', context)
