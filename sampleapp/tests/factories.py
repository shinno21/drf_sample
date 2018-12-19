# coding: utf-8
import factory
from sampleapp import models


class PostStatusFactory(factory.django.DjangoModelFactory):
    """PostStatus のFactory
    """
    class Meta:
        model = models.PostStatus
        django_get_or_create = ('cd',)
    cd = factory.Sequence(lambda n: '%d' % n)
    name = factory.Sequence(lambda n: 'status{0}'.format(n))


class PostFactory(factory.django.DjangoModelFactory):
    """Post のFactory
    """
    class Meta:
        model = models.Post
    title = factory.Sequence(lambda n: 'test title {0}'.format(n))
    content = factory.Faker('text')
    cre_date = factory.Faker('date')
    status = factory.SubFactory(PostStatusFactory)
    username = factory.Sequence(lambda n: 'user{0}'.format(n))


class CommentFactory(factory.django.DjangoModelFactory):
    """Comment のFactory
    """
    class Meta:
        model = models.Comment
    post = factory.SubFactory(PostFactory)
    content = factory.Faker('text')
    username = factory.Sequence(lambda n: 'user{0}'.format(n))
