Melissa And Vik's Wedding App
=========================================

REQUIREMENTS
-------------
MYSQL 5

PYTHON 2.7
setuptools
easy_install
Django 1.3

Development:
-----------
- Create virtualenv
    $cd /home/app
    $mkdir .virtualenv
    $cd .virtualenv
    $virtualenv --no-site-packages wedding 
    $source .virtualenv/wedding/bin/activate

- Install App
    $cd appDir
    $python setup.py install

- Start appserver
    $python manage.py runserver 127.0.0.1:8080

- To run tests:
    Change to webapp directory and issue the following command:
    $python manage.py test site

