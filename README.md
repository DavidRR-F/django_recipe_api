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