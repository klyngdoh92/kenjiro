#!/bin/bash

set -e

cd /home/ubuntu/kenjiro

git pull origin master

docker compose -f docker-compose.yml -f docker-compose.prod.yml up --build -d

docker compose -f docker-compose.yml -f docker-compose.prod.yml exec -T backend python manage.py migrate

docker compose -f docker-compose.yml -f docker-compose.prod.yml exec -T backend python manage.py collectstatic --noinput