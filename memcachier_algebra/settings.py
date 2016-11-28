# Django settings for MemCachier django example.
import os

## MemCachier Settings
## ===================
# Docs: http://github.com/memcachier/django-ascii
#       https://docs.djangoproject.com/en/1.6/topics/cache
if os.environ.get('DEVELOPMENT', None):
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
        }
    }
else:
    # Configure server credentials
    os.environ['MEMCACHE_SERVERS'] = os.environ.get('MEMCACHIER_SERVERS', '').replace(',', ';')
    os.environ['MEMCACHE_USERNAME'] = os.environ.get('MEMCACHIER_USERNAME', '')
    os.environ['MEMCACHE_PASSWORD'] = os.environ.get('MEMCACHIER_PASSWORD', '')

    # Configure cache settings
    CACHES = {
        'default': {
            'BACKEND': 'memcachier_django.ascii.MemcacheCache',
            'OPTIONS': {
                # Enable faster IO
                'no_delay': True,
                # Timeout for set/get requests
                'connect_timeout': 2.5,
                'timeout': 1.5,
                'ignore_exc': True,
            }
        }
    }

## ======================================================================
## EVERYTHING BELOW IS CONFIGURATION UNRELATED TO THIS MEMCACHIER EXAMPLE
## ======================================================================

## Database Settings (none)
## ========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

## Static Assets & Heroku
## ======================
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'static')
]
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

## Templates
## =========

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

## Other Settings
## ==============
DEBUG = True
ADMINS = ()
MANAGERS = ADMINS
TIME_ZONE = 'America/Los_Angeles'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
MEDIA_ROOT = ''
MEDIA_URL = ''

# Allow all host headers
ALLOWED_HOSTS = ['*']

SECRET_KEY = 'l&amp;nd6u%i-s)2c)s5=^i2#v*4)%i9j-g^yo=)z#(#+5pe)o_=%v'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'memcachier_algebra.urls'

WSGI_APPLICATION = 'memcachier_algebra.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

TEST_RUNNER = 'django.test.runner.DiscoverRunner'
