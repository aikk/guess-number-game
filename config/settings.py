DEBUG = True
SECRET_KEY = 'SECRET'
ROOT_URLCONF = 'config.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'guess_game.db',
    }
}


INSTALLED_APPS = [
    'game',
    'django.contrib.auth',
    'django.contrib.contenttypes',
]

STATIC_URL = '/static/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True
    }
]
