**Sistema de Gestión de Tareas**

 - Python
 - Django
 - PostgreSQL
 - Celery
 - Redis

install redis
 [Redis Docs](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/)

install requirements

     ➜ pip3 install -r requirements.txt

run project

     ➜ python3 manage.py runserver --settings=config.settings.development
 
run celery

    ➜ celery -A config.settings.celery.app worker --loglevel=info


Virtual Environments

    SECRET_KEY
    
    DB_NAME
    DB_HOST
    DB_PORT
    DB_USER
    DB_PASSWORD
    
    CELERY_BROKER_URL
    
    EMAIL_BACKEND
    EMAIL_USE_TLS
    EMAIL_HOST
    EMAIL_PORT
    EMAIL_HOST_USER
    EMAIL_HOST_PASSWORD
    DEFAULT_FROM_EMAIL