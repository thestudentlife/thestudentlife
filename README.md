The New TSL Website
===================

Running Locally/Selenium Tests
--------------------------

- Clone this repository
- Navigate to this project's root directory on your computer
- Install [Python 3.4+](https://www.python.org/downloads/)
- Enter <code>bash setup.sh</code>
- Check out localhost:8000 on your favorite browser
- Check out localhost:8000/workflow (Login: kshikama, Password: tsl)


Virtual Machine Configuration Instructions (Outdated)
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

- Install Solr 4.10.2 and run it (if you want to test the search functionality)