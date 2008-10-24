import os
DIRNAME = os.path.dirname(__file__)

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = ':memory:'

ROOT_URLCONF = 'notices.tests.urls'

TEMPLATE_DIRS = (
    DIRNAME,
)

INSTALLED_APPS = (
    'notices',
    'notices.tests',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',

    'notices.context_processors.notices',
)

SECRET_KEY = '8317g=(AD/FGA/G=ASUG=AHSGha0g234hgQ7gAAFASfa3)!%'

NOTICE_TYPES = ('success', 'notice', 'error')
