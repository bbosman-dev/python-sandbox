# StudentCourse app

SURF Assessment for Bram Bosman

This app provides a basic setup to store data for students, courses,
and students taking courses.
It builds two docker containers; one for the postgres database,
the other for the web app with REST api functionality and
basic authentication.

## Starting the app
After cloning the repository, go to project root
and start up the containers:
````
docker-compose build
docker-compose up
````

## Create admin
In another terminal window/tab:
````
docker exec -it surf_web_1 sh
````
In that shell:
````
python manage.py createsuperuser
````
(or 'python3', depending on your setup)

Enter username, email and password.


## API
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

## Database data
Stored in:
````
/postgres-data
````
