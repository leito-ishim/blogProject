from django.shortcuts import render
from django.views.generic import ListView, DeleteView, DetailView
from .models import Article


# Create your views here.
class ArticleListView(ListView):
    model = Article = Article
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail.html'
