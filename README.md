# hh-project
for running this project you should have docker engine installed on your host machine
if you have that then follow the commands bellow

- docker compose up --build

and you will set up the environment on docker and start the project 
simply copy and paste the url bellow on your browser

- http://127.0.0.1:8000

the project will show up 

some helpful commands
list the running docker containers
- docker ps

by this command you will access to the cli of the wppdjango service container
- docker exec -it webpageparser_wppdjango_1 bash
run 
- python manage.py migrate
- python manage.py makemigrations

To enter the cli of pgqldb service container
- docker exec -it webpageparser_pgqldb_1 psql -U postgres
