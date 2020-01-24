# Django Restframework Starter Kit

## Django Restframework の初心者向けスターターキット

* すぐに起動できるコード
* 利用しそうなサンプルコードを含む

## 開発環境

```
# 必要なライブラリのインストール
pip install -r requirements_dev.txt

# 開発環境での起動方法
python manage.py makemigrations --settings=drf_sample.local_settings
python manage.py migrate --settings=drf_sample.local_settings
python manage.py loaddata sampleapp/fixtures/PostStatus.json --settings=drf_sample.local_settings
python manage.py runserver --settings=drf_sample.local_settings
```

## 動作保証

* Python 3.8.0(※)

* ※ 利用しているバージョンで動かない場合は、DjangoとDjango Restframeworkをダウングレードしてください

## 必要なライブラリ

* requirements.txt アプリケーションの稼働に必要なライブラリのリスト（プロダクション環境ではこちらを利用）
* requirements_dev.txt 開発に必要なユーティリティを上記に加えた


## テストについて

* 以下参照
* https://qiita.com/shinno21/items/a42eea9b6ce959e106c0