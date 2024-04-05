Django Setup Wiki

Instructions for setting up Django projects.

Table of Contents

General Setup for all Django Projects
Django REST Framework
Django GraphQL
Django MongoDB
Full-Stack Django (with templates)
General Setup for all Django Projects

Recommended Technologies

Django 3.x
Poetry
Postgres: You can use MySQL or SQL Lite, but Postgres is recommended by the Django official docs. The only exception is if you want to use MongoDB or another NoSQL database with your project. You can find details for that below.
Initial Setup

Must have Python 3, Django, and Postgres version 12.x installed

Make sure Postgres is running on your machine

django-admin startproject [projectname]

Create a virtual environment: python -m venv venv

Go into your virtual environment: source venv/bin/activate

Run poetry init -> This will create a TOML file for you with your project config where Poetry will add your dependencies

Install psycopg2-binary: poetry add psycopg2-binary

Rename the [projectname] folder to config

Create a folder named apps

Create an __init__.py file inside of the apps folder

Users Setup

Create a users app: mkdir apps/users and then python manage.py startapp users apps/users
Make sure you add apps.users to installed apps in the settings.py file
Also, if you are using an apps folder as I recommend in this wiki, you will need to change the name of every Django app in the apps.py file: e.g. from name = users to name = apps.users
Setup custom User model and custom user manager: https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#a-full-example
AUTH_USER_MODEL = 'users.User'
Set up admin interface for User model:
from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_admin')


admin.site.register(User, UserAdmin
Database Setup

Postgres is optional, but recommended in the official Django docs.

Setup Postgres in Django settings.py file:
'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': '[dbname]',
    'USER': '[dbadmin]',
    'PASSWORD': '',
    'HOST': 'localhost',
    'PORT': '',
}
Setup Database in Postgres
Create the database: CREATE DATABASE [dbname];
Create DB user: `CREATE USER [dbadmin];
Grant privilages to user for our database: GRANT ALL PRIVILEGES ON DATABASE coducat TO [dbadmin];
Run migrations: python manage.py migrate
More Setup

Create an admin user for logging into the Django admin interface: python manage.py createsuperuser
Run the app: python manage.py runserver
View the API at localhost:8000 and the admin interface at localhost:8000/admin
Django REST Framework

This builds off of the general Django setup steps.

Technologies

Django REST Framework
REST Framework Setup

Install the REST Framework with Poetry: poetry add djangorestframework
Set up Django REST Framework
Add DRF to INSTALLED_APPS: 'rest_framework'
Add DRF URLs to urlpatterns: path('', include('rest_framework.urls')),
You can run the Django app normally: python manage.py runserver
Now go to localhost:8000 in your browser and you should see Django REST frameworks default page showing you all the routes you have available to you.
Apps Setup

Create apps
Create Models
Setup Admin interface
Create urls.py file
Setup URLs
Setup Views
Optional Setup

Setup token auth
Setup nested routes: rest_framework_nested
Pagination
Timestamp util for models
Django Graphql

Technologies

Django Graphene
Django GraphQL JWT
Graphiql
Postman
Django MongoDB

Technologies

MongoDB (Running locally)
Djongo
Full-Stack Django

coming soon...
