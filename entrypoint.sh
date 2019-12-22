#!/bin/bash

echo "Apply migrations and basic data creation"
python manage.py migrate
python manage.py loaddata restaurant_menu/fixtures/dishes.json

echo "Starting server"
python manage.py runserver 0.0.0.0:8000
