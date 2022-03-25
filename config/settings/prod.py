from .base import *
# from .sub_settings.http.cors import *
from .sub_settings.system.logs import *

# from .sub_settings.email.gmail import *

from decouple import config

"""
export DJANGO_SETTINGS_MODULE=config.settings.dev
export DJANGO_SETTINGS_MODULE=config.settings.test
export DJANGO_SETTINGS_MODULE=config.settings.stage
export DJANGO_SETTINGS_MODULE=config.settings.prod
"""

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# Database multidatabase
# https://woolbro.tistory.com/82
# https://uiandwe.tistory.com/1252
# https://django-orm-cookbook-ko.readthedocs.io/en/latest/multiple_databases.html

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(ROOT_DIR, "db.sqlite3"),
    },
    # 'mysql_CUD': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'HOST': '127.0.0.1',
    #     'PORT': 3306,
    #     'NAME': 'django_test',
    #     'USER': 'django-test',
    #     'PASSWORD': 'test1324',
    #     'CHARSET': 'utf8',
    #     # 'TEST': {
    #     #     'NAME': 'test1324'
    #     # }
    #     # * 주의 TEST 파라미터는 데이터베이스 사용후 삭제함
    # },
    # 'mysql_R': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'HOST': '127.0.0.1',
    #     'PORT': 3306,
    #     'NAME': 'django_test',
    #     'USER': 'django-test',
    #     'PASSWORD': 'test1324',
    #     'CHARSET': 'utf8',
    #     # 'TEST': {
    #     #     'NAME': 'test1324'
    #     # }
    # },
}

DEBUG='DEBUG_STATE'

ALLOWED_HOSTS = ['ALLOWED_HOSTS_IP']

INSTALLED_APPS += [
    'django_prometheus',
]

'''
django_prometheus는 모든 middleware를 감싸는 형식으로
'django_prometheus.middleware.PrometheusBeforeMiddleware'는 최상단에
'django_prometheus.middleware.PrometheusAfterMiddleware'는 최하단에
정의한다
'''
MIDDLEWARE += []

MIDDLEWARE.insert(0,'django_prometheus.middleware.PrometheusBeforeMiddleware')
MIDDLEWARE.insert(-1,'django_prometheus.middleware.PrometheusAfterMiddleware')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
# STATIC_DIR = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = [
#     STATIC_DIR,
# ]
# OR
# STATICFILES_DIRS = [
#     BASE_DIR / 'static'
# ]

# static url로 접근했을 때 연결되는 위치 정의
# static 파일을 한 곳에 모아서 서비스 할 경우 상위 STATICFILES_DIRS 변수는 불필요함

STATIC_ROOT = os.path.join(ROOT_DIR, "static")

# python manage.py collectstatic

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(ROOT_DIR, "media")
