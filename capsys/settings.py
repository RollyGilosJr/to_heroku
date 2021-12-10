




"""
Django settings for capsys project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import datetime as dt
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NEW_BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print('basedir', NEW_BASE_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd3tf8$tfd$85mp)i5$om(x0^5#y_733q@f3l+#78&vzg=%d@fz'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False

# ALLOWED_HOSTS = ['capsys.pythonanywhere.com']
#
DEBUG = True

# ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = ['capsys-test.herokuapp.com']

# For Messaging
from django.contrib.messages import constants as messages


#For Axes Backend
AUTHENTICATION_BACKENDS = [
    # AxesBackend should be the first backend in the AUTHENTICATION_BACKENDS list.
    'axes.backends.AxesBackend',

    # Django ModelBackend is the default authentication backend.
    'django.contrib.auth.backends.ModelBackend',
]



# Application definition

INSTALLED_APPS = [
    # 'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'verify_email.apps.VerifyEmailConfig',
    'crispy_forms',
    'main.apps.MainConfig',
    'register.apps.RegisterConfig',
    'submissions.apps.SubmissionsConfig',
    'forum.apps.ForumConfig',
    'guide.apps.GuideConfig',
    'proposalgroup.apps.ProposalgroupConfig',
    'proposaltitle.apps.ProposaltitleConfig',
    'proposalpanelists.apps.ProposalpanelistsConfig',
    'evaluation.apps.EvaluationConfig',
    'feedback.apps.FeedbackConfig',
    'plagiarism_checker.apps.PlagiarismCheckerConfig',
    'manuscriptevaluations.apps.ManuscriptevaluationsConfig',
    'widget_tweaks',
    'axes',
   
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.AxesMiddleware',
]

AXES_LOGIN_FAILURE_LIMIT = 4
AXES_LOCK_OUT_AT_FAILURE = True
delta = dt.timedelta(minutes=3)
AXES_COOLOFF_TIME = delta
AXES_LOCKOUT_TEMPLATE = "main/loginlimitattempts.html"



ROOT_URLCONF = 'capsys.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'capsys.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Manila'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = "/static/"



STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

if not DEBUG:
    print("here1")
    # STATICFILES_DIRS = (
    #     os.path.join(BASE_DIR ,'static'),
    # )
    print('staticfilesdir')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
else:
    print("here2")
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

LOGIN_URL = '/login/'
CRISPY_TEMPLATE_PACK = "bootstrap4"

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'

if DEBUG:

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' # During development only
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = 'huwanmatteo@gmail.com'
    EMAIL_HOST_PASSWORD = 'ugll psjm onwt cxpp'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True

    DEFAULT_FROM_EMAIL = 'noreply<no_reply@capsys.com>'




