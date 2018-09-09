# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#==========把app统一放到apps文件夹=========
import sys
import os.path
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
#=======================================

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x6t!q2ecc(k%h=!fws57w%om^&my$z&ei#9vvx1m0cj9vi!3^9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #===应用模块添加====
    'shop', #商品
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #====调试模式关闭csrf认证==============
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ccxshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #===这里修改了django默认的模板html路径=======
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ccxshop.wsgi.application'


#=======数据库MySQL配置==========

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ccxshop',
        'HOST':'127.0.0.1',
        'PORT':3306,
        'USER':'ccx',
        'PASSWORD':'ccxcsysky',
    }
}
#==============================

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# 修改语言中文后台
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# 静态资源路径 (CSS, JavaScript, Images)
STATIC_URL = '/static/'
# 添加静态资源路径 --------BASE_DIR 是项目的绝对地址
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]