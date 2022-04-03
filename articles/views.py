from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template import loader
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from articles.forms import ArticleForm
from articles.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'articles.html'
    context_object_name = 'articles'

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['list'] = Article.objects.all()
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_form.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super(ArticleCreateView, self).form_valid(form)


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_form.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super(ArticleUpdateView, self).form_valid(form)


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('home')


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"
