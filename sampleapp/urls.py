# coding: utf-8
from django.conf.urls import include
from django.conf.urls import url

from rest_framework import routers

from sampleapp.views.post_views import PostViewSet

app_name = "sampleapp"

router = routers.DefaultRouter()
router.register(r'post', PostViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),

]
