#!/usr/bin/env bash
set -e

export DEBIAN_FRONTEND=noninteractive
if [ -f /root/apt.update ]; then
    filemtime=`stat -c %Y /root/apt.update`
    currtime=`date +%s`
    diff=$(( (currtime - filemtime) / 86400 ))
    if [ $diff -gt 3 ]; then
        echo "Last update more than 3 days ago, running apt-get update"
        apt-get -y update
        touch /root/apt.update
    else
        echo "Recently ran apt-get update ($diff days ago), skipping apt-get update"
    fi
else
    echo "First boot...running apt-get update"
    apt-get -y update
    touch /root/apt.update
fi

apt-get install -y build-essential git libpq-dev nginx supervisor python3-setuptools python3-dev
easy_install3 pip
pip install virtualenv

if [ ! -d "/root/ve" ]; then
    virtualenv -p /usr/bin/python3 -q /root/ve
    echo "Virtualenv created."
fi

source /root/ve/bin/activate

if [ ! -f "/root/ve/updated" -o /vagrant/requirements.txt -nt /root/ve/updated ]; then
    pip install -r /vagrant/requirements.txt
    touch /root/ve/updated
    echo "Requirements for TSL installed"
fi

cd /vagrant
rm -rf db.sqlite3
touch db.sqlite3
rm -rf workflow/migrations/*
touch workflow/migrations/__init__.py
rm -rf mainsite/migrations/*
touch mainsite/migrations/__init__.py
python3 manage.py makemigrations
cp website/data_migration_initial.py workflow/migrations/data_migration_initial.py
python3 manage.py migrate
cp /vagrant/vagrant/tsl.com /etc/nginx/sites-available/tsl.com
rm -rf /etc/nginx/sites-enabled/*
ln -s /etc/nginx/sites-available/tsl.com /etc/nginx/sites-enabled/tsl.com
service nginx restart