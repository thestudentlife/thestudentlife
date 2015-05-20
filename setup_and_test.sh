
rm -rf db.sqlite3;
touch db.sqlite3;
cd workflow && mkdir migrations;
cd ..;
rm -rf workflow/migrations/*;
touch workflow/migrations/__init__.py;
rm -rf mainsite/migrations/*;
cd mainsite && mkdir migrations;
touch mainsite/migrations/__init__.py;
cd ..;
python manage.py makemigrations;
cp website/data_migration_initial.py workflow/migrations/data_migration_initial.py;
mkdir media/
mkdir website/media/photo/;
mkdir website/media/thumbs/;
rm -rf website/media/photo/*;
rm -rf website/media/thumbs/*;
python manage.py migrate;
python manage.py collectstatic --noinput;
python manage.py test;
