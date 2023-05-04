# django_recipe_api
Basic Full Stack Django Project

run linting

```
docker-compose run --rm app sh -c "flake8"
```
***Add #noqa to ignore empty files***

run tests
```
docker-compose run --rm app sh -c "python manage.py test"
```

create project 

```
docker-compose run --rm app sh -c "django-admin startproject app ."
```

create app

```
docker-compose run --rm app sh -c "python manage.py startapp <app_name>"
```

run app dev ***locahost:8000***

```
docker-compose up
```

make migration
```
docker-compose run --rm app sh -c "python manage.py makemigrations"
```

create superuser
```
docker-compose run --rm app sh -c "python manage.py createsuperuser"
```

refresh db

```
docker-compose down
docker volume rm django_recipe_api_dev-db-data
docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate"
```