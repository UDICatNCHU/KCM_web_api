"""
Django settings for udic_nlp_API project.

Generated by 'django-admin startproject' using Django 1.10.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nn7tdc25()!5#y8^#u)gf^22kii)nj9x!ejfhqh@86p5$wn$4m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
] + [
    'webpack_loader',
    'djangobower'
] + [
    'kcmApp',
    'kcem',
    'kem',
    'PMIofKCM',
    'swingerApp',
    'udicTfidf'
]

# 這段是小幫手的api插件
INSTALLED_APPS += [
    'timetable', 
    'cphelper',
    'curso',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'udic_nlp_API.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'udic_nlp_API.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

CORS_ORIGIN_ALLOW_ALL = True 

# django-react conf
STATICFILES_DIRS = [
    #This lets Django's collectstatic store our bundles
    os.path.join(BASE_DIR, 'assets'),
]

WEBPACK_LOADER = {
    'INDEX': {
        'BUNDLE_DIR_NAME': 'bundles/index/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats-index.json'),
    },
    'API': {
        'BUNDLE_DIR_NAME': 'bundles/api/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats-api.json'),
    },
    'MEMBER': {
        'BUNDLE_DIR_NAME': 'bundles/member/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats-member.json'),
    }
}

# django-bower allow django use bower to manage front-end library.

BOWER_COMPONENTS_ROOT = BASE_DIR
STATICFILES_DIRS.append(BOWER_COMPONENTS_ROOT)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
)


BOWER_INSTALLED_APPS = (
    'jquery#2.2.4',
    'semantic#2.2.10',
)

# shared word2vec variable
from gensim import models
W2VMODEL = models.KeyedVectors.load_word2vec_format('./med400.model.bin', binary=True)