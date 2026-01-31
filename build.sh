#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate

# CREACIÓN AUTOMÁTICA DEL SUPERUSUARIO
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='jover').exists() or User.objects.create_superuser('jover', 'joverjesusmoreiramero@gmail.com', '123qwekevin')"