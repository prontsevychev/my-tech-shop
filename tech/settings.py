from django.utils.translation import gettext_lazy as _

import environ
import raven

from apps.core import constance


BASE_DIR = environ.Path(__file__) - 2  # (tech-shop/tech/settings.py - 2 = tech-shop/)

env = environ.Env()
environ.Env.read_env(str(BASE_DIR.path('.env')))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('TS_DEBUG', default=False)

# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env('TS_SECRET_KEY')

# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list('TS_ALLOWED_HOSTS', default=[])

# Application definition

INSTALLED_APPS = [
    'modeltranslation',  # to use the admin integration, modeltranslation must be put before django.contrib.admin

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'constance',
    'constance.backends.database',
    'rosetta',
    'phonenumber_field',
    'anymail',
    'widget_tweaks',
    'raven.contrib.django.raven_compat',

    'apps.core',
    'apps.shop',
    'apps.blog',
    'apps.contact',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ENABLE_DEBUG_TOOLBAR = env.bool('TS_ENABLE_DEBUG_TOOLBAR', default=DEBUG)

if ENABLE_DEBUG_TOOLBAR:
    INSTALLED_APPS += ['debug_toolbar', ]
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

ROOT_URLCONF = 'tech.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR('templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'constance.context_processors.config',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'apps.shop.context_processors.cart_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'tech.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': env.db('TS_DATABASE_URL'),
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('en', _('English')),
    ('ru', _('Russian')),
    ('uk', _('Ukrainian')),
]

MODELTRANSLATION_DEFAULT_LANGUAGE = LANGUAGE_CODE

LOCALE_PATHS = (BASE_DIR('locale'),)

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (BASE_DIR('static'),)

STATIC_ROOT = BASE_DIR('public/static')

# Media files

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR('public/media')


# Rosetta settings

ROSETTA_MESSAGES_PER_PAGE = 50

# Send email

EMAIL_USE_TLS = True

EMAIL_BACKEND = env('TS_EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')

ANYMAIL = {
    'MAILGUN_API_KEY': env('TS_MAILGUN_API_KEY'),
    'MAILGUN_SENDER_DOMAIN': env('TS_MAILGUN_SENDER_DOMAIN')
}

DEFAULT_FROM_EMAIL = env('TS_DEFAULT_FROM_EMAIL', default='noreply@mg.tech-shop.ga')

FEEDBACK_EMAILS_RECIPIENTS_LIST = []

# Constance settings

CONSTANCE_ADDITIONAL_FIELDS = constance.ADDITIONAL_FIELDS

CONSTANCE_CONFIG = constance.CONFIG

CONSTANCE_CONFIG_FIELDSETS = {
    'Contact': ('phone', 'address', 'email'),
    'Map coordinates': ('latitude', 'longitude'),
}

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

# Debug-toolbar

# INTERNAL_IPS = ['127.0.0.1']

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
    'SHOW_TOOLBAR_CALLBACK': lambda request: True,  # Теперь INTERNAL_IPS не нужны!
}

# Sentry

RAVEN_CONFIG = {
    'dsn': 'https://3192aed5ca134c34976a790d7b6ba461:d8450f554b7044319471041c223b6a22@sentry.io/1281380',
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    'release': raven.fetch_git_sha(BASE_DIR),
}
