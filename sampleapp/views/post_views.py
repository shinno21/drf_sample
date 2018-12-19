# coding: utf-8
from rest_framework import viewsets

from sampleapp import models
from sampleapp.serializers.post_serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = PostSerializer

    def filter_queryset(self, queryset):
        queryset = super(PostViewSet, self).filter_queryset(queryset)

        if 'title' in self.request.query_params:
            i_title = self.request.GET["title"]
            queryset = queryset.filter(title__istartswith=i_title)
        return queryset
