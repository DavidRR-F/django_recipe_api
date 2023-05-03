# django_recipe_api
Basic Full Stack Django Project

run linting

```
docker-compose run --rm app sh -c "flake8"
```

run tests
```
docker-compose run --rm app sh -c "python manage.py test"
```

create app 

```
docker-compose run --rm app sh -c "django-admin startproject app ."
```

run app dev ***locahost:8000***

```
docker-compose up
```