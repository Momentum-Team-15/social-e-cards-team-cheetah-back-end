#!/usr/bin/env bash
# exit on error
set -o errexit

pipenv install

pipenv run python manage.py migrate ecard 0027_alter_favorite_card_alter_favorite_user
pipenv run python manage.py collectstatic --no-input
pipenv run python manage.py createsuperuser
