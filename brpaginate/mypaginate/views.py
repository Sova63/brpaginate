from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView
from .forms import CommentForm
from .models import Article, Comment
from .services import get_comments_for_article


def article_list(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 4) # Показывать 4 статей на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) #if page_number else paginator.get_page(1)
    return render(request, 'articles/article_list.html', {'page_obj': page_obj})

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'
    paginate_by = 4  # Показывать 4 статей на странице


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'articles/article_detail.html', {'article': article})


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data (**kwargs)
        context['comment_form'] = CommentForm()
        context['comments'] = get_comments_for_article(self.object.pk)
        return context


def create_comment(request, article_id):
    if not request.method == 'POST':
        return redirect('article_detail', pk=article_id)

    form = CommentForm(request.POST)
    if form.is_valid():
        user = request.user
        is_anon = False
        if user.is_anonymous:
            user = None
            is_anon = True
        comment = Comment(
            article_id=article_id,
            user=user,
            is_anon=is_anon,
            text=form.cleaned_data['text']
        )
        comment.save()
    return redirect('article_detail', pk=article_id)