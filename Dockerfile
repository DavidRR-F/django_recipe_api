FROM python:3.9-alpine3.13
# image maintainer info
LABEL maintainer="David Rose-Franklin"
# recommended when running python in docker
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app

WORKDIR /app

EXPOSE 8000
# Creates venv, Upgrade pip, Install Requirements, Postgresql client package
# If dev true add dev requirements
# remove tmp dir (Keeps image lightweight), 
# Add user in image (Best Practice to not use root user)
# Don't create home or password and specify name "django-user"
# install image handling dependecies zlib and jpeg-dev
# create media directory, change owner, and permissions of vol dirs
ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client jpeg-dev && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev zlib zlib-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user && \
    mkdir -p /vol/web/media && \
    mkdir -p vol/web/static && \
    chown -R django-user:django-user /vol && \
    chmod -R 755 /vol 
# Updates path enviroment variable so python commands dont need path extension
ENV PATH="/py/bin:$PATH"

# Switch to new user
USER django-user

