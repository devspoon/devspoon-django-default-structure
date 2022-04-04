from django.db import models
from django.utils import timezone
from django.urls import reverse
# from django.db.models import F

"""
from datetime import datetime
해당 함수는 UTC 기준으로 동작
settings.py의 USE_TZ = True가 되어 있으면 워닝이 발생함 때문에 아래와 같이 사용
"""


class IsDeletedBaseModel(models.Model):
    # slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    # https://runebook.dev/ko/docs/django/ref/models/options
    # https://runebook.dev/ko/docs/django/ref/models/constraints#django.db.models.UniqueConstraint
    class Meta:
        abstract = True
        db_table=''
        verbose_name = ''
        verbose_name_plural = ''
        ordering = ('-created_at',)
        # ordering = [F('author').asc(nulls_last=True)]

        # indexes = [
        #     models.Index(fields=['last_name', 'first_name']),
        #     models.Index(fields=['first_name'], name='first_name_idx'),
        # ]

        # UniqueConstraint()


    def __str__(self):
        ...
        # return self.title if self.title else self.url
        # return str(self.title) # None 객체가 스트링으로 변환되기 때문에 에러를 피할 수 있음

    def get_apsolute_url(self):
        ...
        # return reverse('shop:product_detail', args=[self.id,self.slug])

    def set_delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

