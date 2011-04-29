# Django settings for ostis project.
import os

def rel(*x):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *x).replace('\\','/')

DEBUG = True
TEMPLATE_DEBUG = DEBUG
COMPRESS = True
ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

CATALOG_IPCOMPONENTOV='E:/Development/Tools/msysgit/msysgit/projects/IP-LIB-SERV/ip-structure/components'

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'iplib', # Or path to database file if using sqlite3.
        'USER': 'root', # Not used with sqlite3.
        'PASSWORD': 'root', # Not used with sqlite3.
        'HOST': 'localhost', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/static_media/static_media.lawrence.com/static_media/"
MEDIA_ROOT = rel('media')

# URL that handles the static_media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://static_media.lawrence.com/static_media/", "http://example.com/static_media/"
MEDIA_URL = '/media/'


# Absolute path to the directory static_media files should be collected to.
# Don't put anything in this directory yourself; store your static_media files
# in apps' "static_media/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/static_media/static_media.lawrence.com/static_media/"
STATIC_ROOT = ''

# URL prefix for static_media files.
# Example: "http://static_media.lawrence.com/static_media/"
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'
# URL prefix for admin static_media files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static_media/admin/", "/static_media/admin/".


# Additional locations of static_media files
STATICFILES_DIRS = (
    rel('static'),
)

# List of finder classes that know how to find static_media files in
# various locations.
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
   # "django.contrib.staticfiles.finders.DefaultStorageFinder",
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
)
# Make this unique, and don't share it with anybody.
SECRET_KEY = 'j5e6omuu%x(ni$wken0yi!unv+%lkh3(i%lu8^%&zqk^9ne+r)'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

DEFAULT_FILE_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'iplib.urls'

TEMPLATE_DIRS = (
        rel('templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'iplib.app',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
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

# CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
