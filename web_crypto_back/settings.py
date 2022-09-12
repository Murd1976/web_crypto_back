"""
Django settings for web_crypto_back project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-t1ff&v5%0(b$t6)*wcp=%_9dni_6qrjwc92q58kxorznt*iko+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []  #["node8083-ft-stable.node.cloudlets.zone"]

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'crypto.backtest@gmail.com'
EMAIL_HOST_PASSWORD = 'fmpgfmwpotmbtwlx'
EMAIL_PORT = 587

# Application definition

INSTALLED_APPS = [
    'crypto_back.apps.Crypto_backConfig',   
#    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
#    'menus',
#    'sekizai',
#    'treebeard',
#    'djangocms_text_ckeditor',
#    'filer',
    'easy_thumbnails',
    'bootstrap4',
#    'djangocms_bootstrap4',
#    'djangocms_bootstrap4.contrib.bootstrap4_alerts',
#    'djangocms_bootstrap4.contrib.bootstrap4_badge',
#    'djangocms_bootstrap4.contrib.bootstrap4_card',
#    'djangocms_bootstrap4.contrib.bootstrap4_carousel',
#    'djangocms_bootstrap4.contrib.bootstrap4_collapse',
#    'djangocms_bootstrap4.contrib.bootstrap4_content',
#    'djangocms_bootstrap4.contrib.bootstrap4_grid',
#    'djangocms_bootstrap4.contrib.bootstrap4_jumbotron',
#    'djangocms_bootstrap4.contrib.bootstrap4_link',
#    'djangocms_bootstrap4.contrib.bootstrap4_listgroup',
#    'djangocms_bootstrap4.contrib.bootstrap4_media',
#    'djangocms_bootstrap4.contrib.bootstrap4_picture',
#    'djangocms_bootstrap4.contrib.bootstrap4_tabs',
#    'djangocms_bootstrap4.contrib.bootstrap4_utilities',
#    'djangocms_file',
#    'djangocms_icon',
#    'djangocms_link',
#    'djangocms_picture',
#    'djangocms_style',
#    'djangocms_googlemap',
#    'djangocms_video',
#    'cms',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTH_USER_MODEL = 'crypto_back.AdvUser'

ROOT_URLCONF = 'web_crypto_back.urls'


TEMPL_DIR = os.path.join(BASE_DIR, 'web_crypto_back', 'templates')
CONF_DIR = os.path.join(BASE_DIR, 'crypto_back', 'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPL_DIR, CONF_DIR,],
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

WSGI_APPLICATION = 'web_crypto_back.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'crytpo_back.db',
    }
}

SITE_ID = 1

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'web_crypto_back', 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

