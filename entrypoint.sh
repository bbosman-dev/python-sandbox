#!/bin/sh

if [ "$DATABASE" = "postgres" ]; then
    echo "Waiting for postgres..."

    while ! nc -z postgres 5432; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Make migrations and migrate the database.
echo "Making migrations and migrating the database. "
python3 manage.py makemigrations main --noinput
python3 manage.py migrate --noinput
echo "Creating superuser admin. "
python3 manage.py createsuperuser --email admin@surfsite.com --username admin --password lantarenpaal.Glazenwasser10


exec "$@"
