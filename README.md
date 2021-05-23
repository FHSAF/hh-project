# hh-project
for running this project you should have docker engine installed on your host machine
if you have that then follow the commands bellow

- docker compose up --build

and you will set up the environment on docker and start the project 
simply copy and paste the url bellow on your browser

- http://127.0.0.1:8000

the project will show up 

list the running docker containers
- docker ps

By this command you will access to the cli of the wppdjango service container
- docker exec -it [name of server service container] bash

There you can run django project commands like
- python manage.py migrate
- python manage.py makemigrations
- python manage.py createsuperuser

To enter the cli of pgqldb service container
- docker exec -it [name of database service container] psql -U postgres
