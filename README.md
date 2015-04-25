The New TSL Website
===================

Basic Configuration Instructions
--------------------------

- Clone a copy of this repository
- Navigate to project's root directory
- Install python3 and pip (the rest of the dependencies will be taken care of)
- Run the reset_database_3.sh script
- Run python manage.py runserver
- Check out localhost:8000 on your favorite browser
- Check out localhost:8000/workflow (Login: kshikama, Password: tsl)

Optional Configuration Items (Will Be Added Later)
--------------------------------------------------

- Install a copy of CKEditor and put it in workflow/static/ (if you want to use the CKEditor when editing articles)
- Install Solr 4.10.2 and run it (if you want to test the search functionality)