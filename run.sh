python manage.py makmigrations
python manage.py migrate
gunicorn --bind=0.0.0.0 --timeout 600 rituBack.wsgi