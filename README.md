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