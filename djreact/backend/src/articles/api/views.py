"""Serializer to convert to json"""

from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import ArticleSerializer
from articles.models import Article

"""creating article list view"""


class ArticleListView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
