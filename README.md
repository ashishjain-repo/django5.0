### Pip upgrade command
`python -m pip install pip`

# Installations 
Create a directory where you want to start your project and switch to that folder. First create a virtual environment using PIP, use this command to create an environment `python -m venv env-name`. Now we are going to install the dependencies in our environment, but to do that we have to run our environment first using this command from the same directory `.\venv\Scripts\activate`. To install Django use command `pip install django`, make sure whenever you are installing any dependencies it should be in the environment.

# Create Project
To create the project you use this command, make sure you are in the environment `django-admin startproject project-name .`. The dot at the end of the command is to tell django to create in the project in the same directory. It will create a folder with the project name and some files which are 
```
__init__.py
asgi.py
settings.py
urls.py
wsgi.py
```

# Understading Configuration Files
`__init__.py` this file tells python that this should be considered as a python package. `asgi.py` & `wsgi.py` these both interfaces allow web servers to communicate with python we application, but they both server different purpose. 'Asgi' stands for Asynchronus Server Gateway InterFace and 'Wsgi' stands for Web Server Gateway Interface. `settings.py` contains all the configuration setting for Django project. `urls.py` is Universal Resource Location which will contain all the endpoints we should have for our application. `manage.py` in the root directory of the project is used for the shell commands for our project.

# Project vs Apps
A project is the core of the Django Application and a project can contain multiple applications. For example one project can have applications like blog, accounts etc.

# Creat Application
To create an application we will be using Manage.py file which will help us to create an application using the core libraries of Django. This command is used to create project: `python manage.py startapp app-name`. This will create an app for us in the root rpoject directory which will contain these files:-
```
migrations
|
-- __init__.py
__init.py__
admin.py
apps.py
models.py
tests.py
views.py
```