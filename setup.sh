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
mkdir website/media/;
mkdir website/media/photo/;
mkdir website/media/thumbs/;
rm -rf website/media/photo/*;
rm -rf website/media/thumbs/*;
python3 manage.py migrate;
python3 manage.py loaddata website/fixtures/initial_data.json;
python3 manage.py collectstatic --noinput;