"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-ru253ifo!7r#+(iu(r)(ci-+w44h#@%z2=c7$g47kfj=%@b*a3"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# 웹에서 도메인 또는 이미지 주소 설정 
ALLOWED_HOSTS = ['127.0.0.1']


# Application definition
#  앱이 만들어지면 이곳에 항상 등록하기 
INSTALLED_APPS = [
    "ml",
    "mysqlapp",
    "frontapp",
    "secondapp",
    "firstapp",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"
# html 파일을 관리할 위치 지정 
# BASE_DIR/'templates'
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR/'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
# 데이터베이스 연결 설정하는 곳 
DATABASES = {
    # SQLite3 데이터 베이스는 디폴트로 사용 
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    # MySQL DB Server 연동
    ## "ENGINE" : 데이터베이스 엔진 연결 
    ## "NAME" : DB 이름
    ## "USER" : 사용자 이름
    ## "PASSWORD" : 패스워드 
    ## "POST" : 로컬 주소
    ## "PORT" : mysql 연결 포트 
    # mysql 패키지 설치 해야 함 : pip install mysqlclient 
    'mysql': {
        "ENGINE" : "django.db.backends.mysql",
        "NAME" : 'pknu',
        "USER" : 'pknu',
        "PASSWORD" : '0107',
        "POST" : 'localhost',
        "PORT" : '3306',
    }
    
}

# default가 아닌 다르 DB를 사용 시에는 아래 리스트 추가 
# [DB를 사용할 앱이름.파일이름.클래스이름]
DATABASE_ROUTERS = ['mysqlapp.router.DBRouter', 'secondapp.router.DBRouter', ]

# DB 실행 내용을 프롬포트에서 확인하기 위해 아래 추가 
LOGGING = {
    'version' : 1,
    'disable_existing_loggers' : False,
    
    'handlers' : {
        'console' : {
            'level' : 'DEBUG',
            'class' : 'logging.StreamHandler',
        }
    },
    
    'loggers' : {
        'django.db.backends' : {
            'handler' : ['console'],
            'level' : 'DEBUG',
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

# LANGUAGE_CODE = "en-us"
# 웹에 표시할 언어지정 
LANGUAGE_CODE = "ko-kr"

# TIME_ZONE = "UTC"
# 웹에서 사용할 시간대
TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

# css. js, image 등을 관리할 폴더 지정 
STATICFILES_DIRS = [
    BASE_DIR/'static'
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
