from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.title

    def get_absolute_url(self):
       return reverse('article_detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    article = models.ForeignKey('mypaginate.Article',related_name='comments',on_delete=models.CASCADE)
    user = models.ForeignKey('myusers.User', related_name='comments',on_delete=models.SET_NULL, null=True, blank=True)
    is_anon = models.BooleanField(default=False)
    text = models.TextField('Текст коментария')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def username(self):
        return self.user.username if self.user is not None else 'Анонимный пользователь'

    def save(self,*args,**kwargs):
        if self.user is None:
            self.is_anon = True
        return super().save(*args, **kwargs)

    def __str__(self):
        return  f"{self.article.title} / {self.username}"
