# studentsapp-fastapi-postgres-sqlalchemy

first create your virtualenv

`$ python3 -m venv venv`

activate venv

`$ source venv/bin/activate`

then install requirements

`$ pip install -r requirements.txt`

install postgresql, login and create the database

`CREATE DATABASE <yourDBname>;`

create a .env file in the root folder

`$ touch .env`

and add your postgresql credentials and the app SECRET_KEY to .env file

>ENV_DATABASE='{yourDBname}'\
ENV_HOST='{your host or localhost}'\
ENV_PORT='{your db port or 5432}'\
ENV_USER='{your db user}'\
ENV_PASSWORD='{your db password}'

finally the project run with: 

`$ uvicorn main:app`

open your browser or your REST Client in: 

### list of students
`GET http://localhost:8000/`
### get a student
`GET http://localhost:8000/student/2`
### new student
`POST http://localhost:8000/student`
### update student
`PUT http://localhost:8000/student/3`
### delete a student
`DELETE http://localhost:8000/student/10`
