#!/usr/bin/env bash

cwd=$(pwd)
echo $(pip --version)
pip install virtualenv
if [ ! -d "$cwd/ve" ]; then
    virtualenv -p $(which python3) -q $cwd/ve
    echo "Virtualenv created."
fi

source $cwd/ve/bin/activate

if [ ! -f "$cwd/ve/updated" -o $cwd/requirements.txt -nt $cwd/ve/updated ]; then
    pip install -r $cwd/requirements.txt
    touch $cwd/ve/updated
    echo "Requirements for TSL installed"
fi

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
python3 manage.py makemigrations;
cp website/fixtures/data_migration_initial.py workflow/migrations/data_migration_initial.py;
mkdir website/media/;
mkdir website/media/photo/;
mkdir website/media/thumbs/;
rm -rf website/media/photo/*;
rm -rf website/media/thumbs/*;
python3 manage.py migrate;
python3 manage.py collectstatic --noinput;
python3 manage.py test;
nohup python3 manage.py runserver < /dev/null &
python3 manage.py shell_plus << END
exec(open('scripts/edit_article.py').read())
exec(open('scripts/upload_images.py').read())
END
python3 manage.py dumpdata > website/fixtures/initial_data.json