# coding: utf-8
from django.db import models


class PostStatus(models.Model):
    """投稿のステータス
    """

    cd = models.CharField("コード", max_length=2, primary_key=True)
    name = models.CharField("名前", max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    """投稿
    """

    title = models.CharField("タイトル", max_length=100)
    content = models.CharField("内容", max_length=1000)
    cre_date = models.DateField("作成日時")
    status = models.ForeignKey(
        PostStatus, verbose_name="状況", on_delete=models.SET_DEFAULT, default="10"
    )
    username = models.CharField("ユーザ", max_length=10)


class Comment(models.Model):
    """投稿に対するコメント（１投稿に対して、０～Ｎ個）
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="投稿")
    content = models.CharField("内容", max_length=1000)
    username = models.CharField("ユーザ", max_length=10)
