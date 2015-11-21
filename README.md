The TSL Website
===================

[![Code Climate](https://codeclimate.com/github/thestudentlife/Manhattan-Project/badges/gpa.svg)](https://codeclimate.com/github/thestudentlife/Manhattan-Project)
[![Build Status](https://travis-ci.org/thestudentlife/thestudentlife.svg?branch=master)](https://travis-ci.org/thestudentlife/thestudentlife)

Configuration
--------------------------

- Clone this repository
- Install [Python 3.4+](https://www.python.org/downloads/)
- Copy `website/settings.py.example` to `website/settings.py`
- Enter <code>bash setup.sh</code>
- Check out localhost:8000 on your favorite browser
- Check out localhost:8000/workflow (Login: kshikama, Password: tsl)

Sever Maintenance (Pushing Changes)
---------------------------

- SSH into Peninsula
- Switch to user tsl: `sudo -u tsl -i`
- Change your directory to the tsl repository: `cd thestudentlife`
- Pull in changes from upstream: `git pull origin master`
- Reload gunicorn: `kill -HUP \`cat run/gunicorn.pid\``

Optional Configuration Items
--------------------------------------------------

- Install Solr 4.10.2 and run it (if you want to test the search functionality)