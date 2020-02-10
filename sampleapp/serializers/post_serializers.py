# coding: utf-8
from rest_framework import serializers, fields
from sampleapp import models
from datetime import datetime


class PostSerializer(serializers.ModelSerializer):
    """Post モデルのシリアライザ
    Postモデルの属性に加え、JOIN先のステータス名称と子モデルCommentの数を返す.
    """

    status_name = serializers.CharField(source="status.name", read_only=True)
    comment_cnt = serializers.SerializerMethodField("get_comment_count")
    # ブラウザでテストするときは以下をコメントアウトする
    cre_date = fields.DateField(input_formats=["%Y-%m-%dT%H:%M:%S.%fZ"])

    class Meta:
        model = models.Post
        fields = (
            "id",
            "title",
            "content",
            "cre_date",
            "status",
            "status_name",
            "username",
            "comment_cnt",
        )

    # 子要素のコメントの数を取得して返却する
    def get_comment_count(self, obj):
        return models.Comment.objects.filter(post_id=obj.id).count()

    def validate_cre_date(self, value):
        if value < datetime.today().date():
            raise serializers.ValidationError("作成日は当日以降を入力してください")
        return value
