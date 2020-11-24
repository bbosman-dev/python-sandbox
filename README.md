# StudentCourse app

SURF Assessment for Bram Bosman

To start this dockerized app, after cloning the repository, go to project root
and start up the containers:
````
docker-compose build
docker-compose up
````

To be able to access the admin page:
````
docker exec -it manage.py createsuperuser
````

Enter username, email and password.

The app URL root is
````
localhost:8000
````

Admin page at:
````
localhost:8000/admin/
````

Other api's:
````
/students/
/students/{id}
/courses/
/courses/{id}
/studentcourses/
/studentcourses/{id}
````
