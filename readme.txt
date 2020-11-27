local setup guides.

1) install python and django


2) create the database connection on mysql
  connection name : django.contrib.gis.db.backends.mysql
  hostName : 127.0.0.1
  port : 3306 
  put user name and password as root.
  
  
 3) setup https://trac.osgeo.org/osgeo4w/ in ur local 
 C:\OSGeo4W64
 
 4) now install all the dependecies from requirements.txt
 
 5)python manage.py makemigrations
 
 6)python manage.py migrate
 
 7)python manage.py createsuperuser
      crate ur super user


 8)python manage.py runserver
