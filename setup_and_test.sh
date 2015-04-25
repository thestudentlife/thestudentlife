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
rm -rf workflow/migrations/*;
touch workflow/migrations/__init__.py;
rm -rf mainsite/migrations/*;
touch mainsite/migrations/__init__.py;
python3 manage.py makemigrations;
cp website/data_migration_initial.py workflow/migrations/data_migration_initial.py;
python3 manage.py migrate;
python3 manage.py collectstatic --noinput;
python3 manage.py test;