#! /bin/bash
# Reset db.sqlite3

rm -rf db.sqlite3;
touch db.sqlite3;
python manage.py makemigrations;
python manage.py migrate;
python manage.py test;
#python3 manage.py makemigrations;
#python3 manage.py migrate;
#python3 manage.py test;