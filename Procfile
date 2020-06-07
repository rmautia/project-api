release: python3 manage.py makemigrations ratings
release: python3 manage.py migrate


web: gunicorn pgram.wsgi --log-file -