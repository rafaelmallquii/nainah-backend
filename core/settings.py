"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

CORS_ORIGIN_WHITELIST = [
    'https://nainah.yotohosting.tk',
    # Add other trusted origins if needed
]

CORS_ALLOWED_ORIGINS = [
    'https://nainah.yotohosting.tk',
    # Add other trusted origins if needed
]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9e%o308bxzqagsq#z^52e6@s%@60+8wj+x*k!1g7gb4tyf4@g4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CSRF_ALLOWED_ORIGINS = ['*']

# Application definition

DJANGO_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
]

THIRD_PARTY_APPS = [
    'ckeditor',
    'colorfield',
    'rest_framework',
]

LOCAL_APPS = [
    'chart',
    'customer',
    'category',
    'product',
    'coupon',
    'order',
    'shipment',
    'transaction',
    'newsletter',
    'setting',
    
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en'

# Miami Time Zone
TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# STATIC_URL = 'static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# MEDIA_URL = 'media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, '/static/')
STATIC_URL = 'static/'

# STATICFILES_DIRS = [os.path.join(BASE_DIR, "static/")]

MEDIA_ROOT = f'{BASE_DIR}/media/'
MEDIA_URL = 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Jazzmin settings
JAZZMIN_SETTINGS = {
    "site_title": "NainahCollections",
    "site_header": "NainahCollections",
    "site_brand": "NainahCollections",
    "site_logo": "images/logo.png",
    "site_favicon": "images/logo.png",
    "welcome_sign": "Welcome to NainahCollections",


    "changeform_format": "horizontal_tabs",


    "search_model": ["product.Product"],


    "copyright": "NainahCollections",
    
    "show_ui_builder": False,

    "navigation_expanded": True,

    "hide_apps": [],

    "custom_css": "css/custom.css", 
    "custom_js": "js/custom.js",

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-regular fa-user",
        "auth.Group": "fas fa-users",

        "chart.Chart": "fas fa-chart-pie",
        "coupon.Coupon": "fas fa-regular fa-tag",
        "customer.Customer": "fas fa-user",
        "category.Category": "fas fa-light fa-list",
        "product.Product": "fas fa-regular fa-box",
        "product.Tag": "fas fa-regular fa-hashtag",
        "order.Order": "fas fal fa-shopping-cart",
        "shipment.Shipment": "fas fa-truck",
        "transaction.Transaction": "fas fa-credit-card",
        "newsletter.Newsletter": "fas fa-rss-square",
        "setting.Setting": "fas fa-cog",

    },

    # cambiar el orden de los modelos en el menu 
    "order_with_respect_to": {
        "auth": ["auth.User", "auth.Group"],
        "chart": ["chart.Chart"],
        "customer": ["customer.Customer"],
        "category": ["category.Category"],
        "product": ["product.Product"],
        "coupon": ["coupon.Coupon"],
        "order": ["order.Order"],
        "shipment": ["shipment.Shipment"],
        "transaction": ["transaction.Transaction"],
        "newsletter": ["newsletter.Newsletter"],
        "setting": ["setting.Setting"],
    },

    # buttons 
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-pink",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-light-pink",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success"
    }
}

# default auth user model
AUTH_USER_MODEL = 'customer.Customer'