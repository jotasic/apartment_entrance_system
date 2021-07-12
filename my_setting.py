from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

SECRET_KEY = 'django-insecure-djk5!f55-z)l&dgk#84gj(o*3x1ec0i#$)bw5z(9*ois*=jl4_'