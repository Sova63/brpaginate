from django.contrib import admin
from .models import *
from mypaginate.models import Article


admin.site.register(Article)

