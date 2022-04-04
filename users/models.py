from uuid import uuid4
from django.utils import timezone
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from imagekit.models import ImageSpecField  # 썸네일 함수
from imagekit.processors import ResizeToFill  # 사이즈조절

from django.db import models
from django.db.models import F
from django.contrib.auth.models import AbstractUser

from utils.model_utils import date_upload_to

# Create your models here.


class User(AbstractUser):

    class Gender(models.TextChoices):
        MAN = '0', _('Female')
        WOMAN = '1', _('Male')
        NO_DISCLOSE = '2', _('Not to disclose')

    email = models.EmailField(max_length=200, unique=True, null=True) # it can be null for synchronization of social account
    nickname = models.CharField(verbose_name=_('Nick Name'),null=False, max_length=30)
    gender = models.SmallIntegerField(verbose_name=_('Gender'),choices = Gender.choices, default=Gender.NO_DISCLOSE)
    profile_image = models.ImageField(verbose_name=_('User Profile Image'),upload_to=date_upload_to, default='default/no_img.png')
    photo_thumbnail = ImageSpecField(
        source="profile_image",  # 원본 IageField이름
        processors=[ResizeToFill(500, 325)],  # 사이즈 조정
        format="JPEG",  # 최종 저장 포맷
        options={"quality": 60},  # 저장 옵션
    )

    is_deleted = models.BooleanField(verbose_name=_('Deleted State'),default=False)
    updated_at = models.DateTimeField(verbose_name=_('Updated Time'),auto_now=True,null=True)
    deleted_at = models.DateTimeField(verbose_name=_('Deleted Time'),null=True)

    # USERNAME_FIELD은 user model에서 사용할 고유 식별자, 기본은 id
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname','username']

    class Meta:
        db_table = "abstractuser_user"
        verbose_name = ('user')
        verbose_name_plural = ('users')
        ordering = [F('date_joined'),]
        # ordering = [F('date_joined').desc(nulls_last=True)] # Null 밑으로
        # ordering = [F('-date_joined').asc(nulls_last=True)] # Null 상위로
        constraints = [
            models.UniqueConstraint(fields=['email', 'nickname'], name='unique fields of constraint'),
        ]

    def __str__(self):
        return "%s - %s" % (
            self.username,
            self.nickname,
        )

    def get_full_name(self):
        return f'{self.first_name}{self.last_name}'

    get_full_name.short_description = _('Full name')

    def get_short_name(self):
        return self.nickname

    get_short_name.short_description = _('Name')

    def get_absolute_url(self):
        ...

    def set_delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.email = ''
        self.first_name = ''
        self.last_name = ''
        self.password = ''
        self.deleted_at = timezone.now()
        self.save()

    def set_deactivate(self):
        self.is_active = False
        self.save()