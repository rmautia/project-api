release: python3 manage.py makemigrations rate
release: python3 manage.py migrate


web: gunicorn rate.wsgi --log-file -