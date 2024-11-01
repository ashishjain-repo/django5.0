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
|__ __init__.py
__init.py__
admin.py
apps.py
models.py
tests.py
views.py
```

# Application File Structure
`admin.py` we are going to register our models here which is a blueprint of our data. `apps.py` is the configuration file for our application. `tests.py` where we are going to write tests for your application, and `views.py` where we receive request from user and then perform operation on it.

# Additional File
Our app does not have it's own urls.py file so we have to create another urls.py in the root of the app.

# Foodie Sandbox App
We’ve created a Django project named "foodie" and an app called "sandbox", with urls.py added for URL routing. First, we import path from django.urls, which will be used in urlpatterns—a list containing URL patterns. The path function, which takes a route, view, kwargs, and a name, defines these patterns. Since the pattern needs a view, we import the views from the current app, and for now, we’ll create a simple view function.

In views.py, we define a function for the root path "/" that accepts a request parameter. To send an HTTP response, we import HttpResponse from django.http. This response will simply return a string, such as "Hello, World!". The view function format will be views.index. Next, we configure the URL in the project’s urls.py so our app’s views can be accessed. The app route will be "sandbox/", and we’ll include the app’s urls.py by importing include.

Lastly, we add "sandbox" to INSTALLED_APPS in settings.py, which registers the app with the project. Now, running `python manage.py` runserver will start the server and let us view the results.

# Django MVT Architecture
In MVT architecture we define the urls, write the views to create the logic that can be shown in the template.