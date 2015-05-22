The New TSL Website
===================

Running Locally/Selenium Tests
--------------------------

- Navigate to project's root directory
- Install [Python 3.4+](https://www.python.org/downloads/)
- Enter <code>bash simple_setup_and_test.sh</code>
- Enter <code>python3 manage.py runserver</code> or <code>python manage.py runserver</code> to start up website
- Check out localhost:8000 on your favorite browser
- Check out localhost:8000/workflow (Login: kshikama, Password: tsl)

Note you must have Firefox to run the Selenium tests


Basic Virtual Machine Configuration Instructions
--------------------------

- Clone a copy of this repository
- Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- Install [Vagrant](https://www.vagrantup.com/downloads.html)
- Open up a terminal window
- Navigate to project's root directory
- Enter <code>vagrant up</code> (to set up the virtual machine)
- Enter <code>vagrant ssh</code> (to connect to the virtual machine)
- Enter <code>bash /vagrant/vagrant/run.sh</code> (to start up website)
- Check out 192.168.33.10 on your favorite browser

Optional Configuration Items (Will Be Added Later)
--------------------------------------------------

- Install a copy of CKEditor and put it in workflow/static/ (if you want to use the CKEditor when editing articles)
- Install Solr 4.10.2 and run it (if you want to test the search functionality)