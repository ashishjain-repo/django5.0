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
Now we have created a project named foodie and an app named sandbox. We have also added the urls.py in our app. Now we have to provide some url patterns for this app. First we are going to import path from django.urls. This path will be passded in the urlpatterns which is a list and path function takes multiple arguments which are a route, view, kwargs, and string. We have to follow this pattern in order to make this path or url or route work. Since we have to pass views in the pattern we have to import the views from our current app. View is currrently empty so now we have to define a function for the view with path "/" it means root and we have to pass a parameter request. We are going to create a function in the view and for now we are going to return a Http respose for which we have to import the function called `HttpResonse` which will be coming from `django.Http`. And the response we will send is going to be a string.  So we have to mention the view name following by the function like this `views.index`. Now we have to configure the url of the app in the project so our user can see those views. The route will start with the name of the app and following with the route inside which we defined in the app. So our main root for app is "/" but for out project it is "sandbox/". We also have to mention that we are including this from the urls file inside the app for which we will import include function inside the project urls.py. Whenever we add a new app we have to configure that in our project settings.py file. Then under installed apps we can add "sandbox" as an app. Now finally we can run our server and see the results by using `python manage.py runserver`.
```

```