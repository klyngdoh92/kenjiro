#!/bin/bash

set -e

cd /home/ubuntu/kenjiro

git pull origin main

docker compose up --build -d

docker compose exec -T backend python manage.py migrate

docker compose exec -T backend python manage.py collectstatic --noinput