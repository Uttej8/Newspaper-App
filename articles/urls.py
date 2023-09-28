from django.urls import path

from .views import *

urlpatterns = [
    path('', ArticleListView.as_view(), name = 'article_list'),
    path('view/<int:pk>/', ArticleDetailView.as_view(), name = 'article_detail'),
    path('edit/<int:pk>/', ArticleEditView.as_view(), name = 'article_edit'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name = 'article_delete'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),
]