#! /bin/bash
# Reset db.sqlite3

rm -rf db.sqlite3;
touch db.sqlite3;
rm -rf mainsite/migrations/*;
touch mainsite/migrations/__init__.py;
rm -rf workflow/migrations/*;
touch workflow/migrations/__init__.py;
python manage.py makemigrations;
python manage.py migrate;
python manage.py shell < website/initial_data.py;
python manage.py shell < website/initial_data_test.py;