from .common import *


DEBUG = True
SECRET_KEY = 'django-insecure-1qj-*kqg4)x-t1py=p)dvh)zaig4sr54_7g&^8t5xx$=k@xpes'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '*********'
    }
}
