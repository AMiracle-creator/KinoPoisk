release: python3 src/manage.py migrate
web: gunicorn kinopoisk.wsgi --chdir src --preload --log-file -