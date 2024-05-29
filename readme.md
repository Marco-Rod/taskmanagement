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
