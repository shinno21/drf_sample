# coding: utf-8
from django.urls import reverse
from django.utils.http import urlencode

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory

from datetime import datetime

from sampleapp import models
from sampleapp.tests import factories
from sampleapp.tests import helpers
from sampleapp.views.post_views import PostViewSet


class PostListTests(APITestCase):
    """Post の検索テスト
    """
    def setUp(self):
        """"各テストメソッド毎の前処理
        マスタデータ登録など、各テストに共通で必要な前準備を記述する
        """
        self.status_close = factories.PostStatusFactory(cd="99", name="無効")
        self.status_open = factories.PostStatusFactory(cd="10", name="有効")

    def tearDown(self):
        """各テストメソッド毎の後処理
        ここでは利用していないが、例えばテスト処理内でファイルを作成した後に削除するとか、テストの後片付けに利用
        ただし、テストで使ったデータは毎回クリアされるので、テスト後のデータ削除はこちらに記述する必要はない
        """
        pass

    def test_search_post(self):
        """Post検索 API で返される全属性の検証
        """
        # テストデータの作成
        p = factories.PostFactory(title="test title",
                                  content="test content...",
                                  cre_date=helpers.today,
                                  status=self.status_open,
                                  username="testuser")
        # 投稿に対するコメントを２件登録する
        factories.CommentFactory(post=p)
        factories.CommentFactory(post=p)

        # APIをリクエストする準備
        factory = APIRequestFactory()
        # リクエストするオブジェクトを準備
        # Viewsetに定義している一覧取得、CRUDのAPIを呼ぶには、
        # 呼びたいas_view内の辞書に以下のリンク先の組み合わせを設定する
        # https://www.django-rest-framework.org/api-guide/routers/#simplerouter
        post_list = PostViewSet.as_view({'get': 'list'})

        url = "".join([
            reverse('sampleapp:post-list')
        ])
        request = factory.get(url)
        response = post_list(request)
        rd = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         "HTTPステータス200が返ること.")
        self.assertEqual(len(rd['results']), 1,
                         "1件取得できること.")

        # ここでは全属性の検証を行うものとする
        self.assertEqual(rd['results'][0]['title'], "test title",
                         "title 属性の検証.")
        self.assertEqual(rd['results'][0]['content'], "test content...",
                         "content 属性の検証.")
        self.assertEqual(rd['results'][0]['cre_date'],
                         datetime.strftime(helpers.today, '%Y-%m-%d'),
                         "cre_date 属性の検証.")
        self.assertEqual(rd['results'][0]['status'],
                         self.status_open.cd,
                         "status_cd 属性の検証.")
        self.assertEqual(rd['results'][0]['username'], "testuser",
                         "testuser 属性の検証.")
        self.assertEqual(rd['results'][0]['status_name'],
                         self.status_open.name,
                         "status_name 属性の検証.")
        self.assertEqual(rd['results'][0]['comment_cnt'], 2,
                         "comment_count属性の検証.")

    def test_search_post_by_title(self):
        """Post検索 API titleによる前方一致の検証
        """
        # テストデータの作成
        factories.PostFactory()
        factories.PostFactory()
        factories.PostFactory(title="abcde")

        factory = APIRequestFactory()
        post_list = PostViewSet.as_view({'get': 'list'})

        # urlの設定
        # ここでは、titleパラメータをクエリ形式で渡す
        # パラメータの渡し方は以下参照
        # https://qiita.com/shinno21/items/daa46a6f5f1df29a24af
        query = urlencode(dict(title="test title"))
        url = "".join([
            reverse('sampleapp:post-list'),
            '?',
            query
        ])
        request = factory.get(url)
        response = post_list(request)
        rd = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         "HTTPステータス200が返ること.")
        self.assertEqual(len(rd['results']), 2,
                         "2件取得できること.")


class PostDetailTests(APITestCase):
    """Post の検索テスト
    """
    def setUp(self):
        """"各テストメソッド毎の前処理
        マスタデータ登録など、各テストに共通で必要な前準備を記述する
        """
        self.status_close = factories.PostStatusFactory(cd="99", name="無効")
        self.status_open = factories.PostStatusFactory(cd="10", name="有効")
    
    def test_create_post(self):
        """Postの登録処理検証
        """
        factory = APIRequestFactory()
        post_cre = PostViewSet.as_view({'post': 'create'})

        params = {
            "title": "登録検証title",
            "content": "登録検証content",
            "cre_date": helpers.tomorrow.strftime("%Y-%m-%d"),
            "status": "10",
            "username": "testuser"
        }

        url = "".join([
            reverse('sampleapp:post-list'),
        ])

        request = factory.post(url, data=params)
        response = post_cre(request)

        post = models.Post.objects.filter(title=params["title"])

        # ステータス確認
        self.assertEqual(response.status_code, status.HTTP_201_CREATED,
                         "HTTPステータス201が返ること.")
        
        self.assertEqual(post[0].title,
                         params["title"],
                         "登録された title が正しいこと.")
        self.assertEqual(post[0].content,
                         params["content"],
                         "登録された content が正しいこと.")
        self.assertEqual(post[0].cre_date.strftime("%Y-%m-%d"),
                         params["cre_date"],
                         "登録された cre_date が正しいこと.")
        self.assertEqual(post[0].status.cd,
                         params["status"],
                         "登録された status が正しいこと.")
        self.assertEqual(post[0].username,
                         params["username"],
                         "登録された username が正しいこと.")
