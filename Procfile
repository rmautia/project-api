release: python3 manage.py makemigrations 
release: python3 manage.py migrate


web: gunicorn peereview.wsgi --log-file -