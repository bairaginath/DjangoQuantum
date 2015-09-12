1)On Ubuntu default python -v 2.7.6
no need to install python

2) install pip (python package mananger)
  $sudo apt-get install python-pip

3) if mysql server is not installed,see following code for install
mysql server
   $sudo apt-get install mysql-server

4) create database named as 'DjangoQuantum' on your local mysql server

5) install the require development packages for python and mysql server
   $sudo apt-get install python-dev libmysqlclient-dev

5) install virtual environment package
   $pip install virtualenv

6)clone this Repository 

7) go to in side DjangoQuantum folder,activity the virtual enviroment as following
   $source bin/activate.

8)in side virutal enviroment,install all dependency software of this project as following
   $pip install -r requirements.txt

9)in side virutal enviroment,move to DjangoQuantum/ folder,run as following for sync database to create all tables (only once,no need to do second time)
   $python manage.py syncdb

10) if run server locally,then run following command as following
    $python manage.py runserver   (by default it runs http://localhost:8000)

11) if run server global,then run following command as following
     $python manage.py runserver 198.162.3.1:9211
