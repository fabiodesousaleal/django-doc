# Installation
    Step-by-step instructions
    
## Install the django-tailwind package via pip:
    python -m pip install django-tailwind


## Add 'tailwind' to INSTALLED_APPS in settings.py:

INSTALLED_APPS = [
  # other Django apps
  'tailwind',
]

## Create a Tailwind CSS compatible Django app, I like to call it theme:
    python manage.py tailwind init

## Add your newly created 'theme' app to INSTALLED_APPS in settings.py:

INSTALLED_APPS = [
  # other Django apps
  'tailwind',
  'theme'
]

## Register the generated 'theme' app by adding the following line to settings.py file:

TAILWIND_APP_NAME = 'theme'

## Make sure that the INTERNAL_IPS list is present in the settings.py file and contains the 127.0.0.1 ip address:

INTERNAL_IPS = [
    "127.0.0.1",
]

## Install Tailwind CSS dependencies, by running the following command:
    python manage.py tailwind install

## The Django Tailwind comes with a simple base.html template located at your_tailwind_app_name/templates/base.html. You can always extend or delete it if you already have a layout.

If you are not using the base.html template that comes with Django Tailwind, add {% tailwind_css %} to the base.html template:

{% load static tailwind_tags %}
...
<head>
   ...
   {% tailwind_css %}
   ...
</head>



python manage.py tailwind start
Check out the Usage section for information about the production mode.