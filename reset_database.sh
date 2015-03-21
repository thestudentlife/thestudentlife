#! /bin/bash
# Reset db.sqlite3

rm -rf db.sqlite3;
touch db.sqlite3;
rm -rf workflow/migrations/*;
touch workflow/migrations/__init__.py;
rm -rf mainsite/migrations/*;
touch mainsite/migrations/__init__.py;
python manage.py makemigrations;
cp website/data_migration_initial.py workflow/migrations/data_migration_initial.py;
python manage.py migrate;
python manage.py test;