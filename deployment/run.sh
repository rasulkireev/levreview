RUN python manage.py collectstatic --noinput
python manage.py migrate
# python manage.py djstripe_sync_models

gunicorn --bind 0.0.0.0:$APP_PORT --workers 3 levreview.wsgi:application
