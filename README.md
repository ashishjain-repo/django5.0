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
In MVT architecture we define the urls, write the views to create the logic that can be shown in the template. More deep understanding of MVT.
* Model (Data Structure)
    1. Define Schema
    2. ORM, database abstraction layer
* View (Business Logic)
    1. Request Handling
* Template (Presentation Layer)
    1. Layout Structure
    2. Seperation of concerns

View is in this case is the middleman which receives the request from the user and based on the logic works with model(database) and templates(static files) and then return the results in the form of template based on the logic.

# Changing Project's Routes and Testing Routes on the browser
URL dispatcher which is the request sent from the user, is always sent to the project not the app, and specifically the urls.py in the project directory, where we defined all the routes when application runs. So we have to remember one thing, whatever route we put in the project urls will be served on the server or browser. So for now we are going to remove the path `sandox/` and leave it empty so whenever we run the server, the root page will be our app, or our app will be served on the root page.

# Passing Data to the Response in our view
It is very simple to pass dynamic data, what we can do it create a variable and pass it the index function that we have created and then in the httpResponse we can use f-string and pass the data which will displayed by the view. We can also do it with using dictionaries, and list, and can perform other functions on data like random and use it inside the function.

- sandbox/views.py
```
from django.shortcuts import render
from django.http import HttpResponse
from random import choice
# Create your views here.

fruits = ['apple','mango','banana']

def index(request):
    data = "Ash"
    data2 = {"name":"Ashish Jain","Profession":"Software Developer"}
    data3 = choice(fruits)
    return HttpResponse(f"Hey {data}! You are a {data2['Profession']}. Random Fruit: {data3.title()}")
```

# Static vs Dynamic Websites
Static websites or pages are the pages that are request by user a HTTP request and what happens is user get the static page, which means user is getting just the fixed static page which will be same everytime that you request that page. In these pages, they need to be manually changed, by the person who is maintainig the page. With the dynamic website that is not the case, now the request is sent by the client, first of all the data itself that is returned is not static itself. This means the content on that page changes depending on the tasks that is being performed by the user. For example when a user logged in the results that are returned are realted to the user, which changes from user to user, because every user does not have the same information.

Django allows you to seperate the front and backend into two different components. So we have frontend which is the client side, or the interface that will be utilized by the user to get the information. Backend is where our application logic resides, which returns the results based on a specific request.

* Front-end (Client-Side) User Interaction
    1. User Interface (UI)
    2. Template (HTML, CSS, JavaScript) 
* Back-end (Server-Side) Application Logic
    1. Database
    2. API's
    3. Views
    4. URL Dispatcher

# Django Settings and URL Dispatcher
`settings.py` This is the file for project configuration for how Django project operates. `URL Dispatcher` this matches various patterns of URLs to the corresponding views.
We have incoming request from user, and then we have a Django URL Resolver which looks up and find the correct view that needs to be called and then it returns either HttpRequest or the template. Those patterns are defined in the root's or Project `urls.py` and if the pattern matches it directly returns the view requested or HttpRequest. If the pattern is mathching on the app level it check and matches the pattern and returns the HttpResonse of returns a template.

# Django Views