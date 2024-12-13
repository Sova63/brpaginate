from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, render
from django.views.generic import ListView
from .models import Article


'''def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {'articles': articles})'''

def article_list(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 6)  # Показывать 10 статей на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'articles/article_list.html', {'page_obj': page_obj})


class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'
    paginate_by = 10  # Показывать 10 статей на странице


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'articles/article_detail.html', {'article': article})



