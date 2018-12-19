# coding: utf-8
from rest_framework import serializers
from sampleapp import models


class PostSerializer(serializers.ModelSerializer):
    """Post モデルのシリアライザ
    Postモデルの属性に加え、JOIN先のステータス名称と子モデルCommentの数を返す.
    """
    status_name = serializers.CharField(source='status.name', read_only=True)
    comment_cnt = serializers.SerializerMethodField('get_comment_count')

    class Meta:
        model = models.Post
        fields = ("id", "title", "content", "cre_date",
                  "status", "status_name", "username", "comment_cnt")

    # 子要素のコメントの数を取得して返却する
    def get_comment_count(self, obj):
        return models.Comment.objects.filter(post_id=obj.id).count()
