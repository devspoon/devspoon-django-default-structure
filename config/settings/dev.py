from .base import *
# from .sub_settings.debug.nose import * #NOSE coverage trace
# from .sub_settings.http.cors import *
from .sub_settings.system.logs import *

# from .sub_settings.email.gmail import *

# from .sub_settings.oauth import *
from decouple import config

# import status checking
# import json
# print(json.dumps(DEFAULT_LOGGING, indent=4, sort_keys=True))

"""
export DJANGO_SETTINGS_MODULE=config.settings.dev
export DJANGO_SETTINGS_MODULE=config.settings.test
export DJANGO_SETTINGS_MODULE=config.settings.stage
export DJANGO_SETTINGS_MODULE=config.settings.prod
"""

DEBUG='DEBUG_STATE'

ALLOWED_HOSTS = ['ALLOWED_HOSTS_IP']

# debug toolbar를 동작시키기 위한 서버 ip 정보를 명시함
INTERNAL_IPS = [
    'IP_ADDRESSES'
]

DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.logging.LoggingPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
]


def custom_show_toolbar(self):
    return True


DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
    "ENABLE_STACKTRACES": True,
    "SHOW_TOOLBAR_CALLBACK": custom_show_toolbar,
}

INSTALLED_APPS += [
    "debug_toolbar",
    "django_nose",
    "silk",
    'django_extensions',
]

# django-extentions로 ERP 만들때 해줘야 하는 설정
GRAPH_MODELS = {
    "all_applications": True,
    "group_models": True,
}

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "silk.middleware.SilkyMiddleware",
]


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

# reference blog : https://velog.io/@kim6515516/Django-silk-%EC%84%B1%EB%8A%A5-%ED%94%84%EB%A1%9C%ED%8C%8C%EC%9D%BC%EB%9F%AC
# reference github : https://github.com/jazzband/django-silk

SILKY_PYTHON_PROFILER = True
SILKY_PYTHON_PROFILER_BINARY = True
