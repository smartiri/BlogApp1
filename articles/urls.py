from django.contrib.auth.decorators import login_required
from django.urls import path, include

from articles.views import ArticleListView, ArticleCreateView, ArticleUpdateView, ArticleDetailView, ArticleDeleteView
urlpatterns = [
    path('', login_required(ArticleListView.as_view()), name='home'),
    path('articles/create/', login_required(ArticleCreateView.as_view()), name='article_create'),
    path('article/<int:pk>', login_required(ArticleDetailView.as_view()), name='article_detail'),
    path('article/update/<int:pk>', login_required(ArticleUpdateView.as_view()), name='article_update'),
    path('article/delete/<int:pk>', login_required(ArticleDeleteView.as_view()), name='article_delete')
]
