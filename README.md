# Django

WSGI is synchronous and best for traditional web apps, while ASGI is asynchronous and designed for real-time, high-concurrency applications like WebSockets and async APIs.
*** Django started with WSGI
1. Modern Django supports ASGI
2. You can still run Django in WSGI mode if:
3. No WebSockets
4. Simple APIs

Use ASGI if:
> WebSockets, 
>  Background tasks, 
> High concurrency

Steps to create first Web App
1. install django
```pip install django```

2. run below command
```django-admin startproject project_name```

3. run the server
```python .\myfirstsite\manage.py runserver```

python manage.py startapp myfirstsite.  
--create a new django app(folder+file)   

### django-admin startproject project_name
This command creates a new Django project.  
A project is the overall configuration and container for your entire Django application. It includes settings, main URL configuration, and deployment-related files.

```
django-admin startproject myproject
```

### Important Files:
manage.py – Command-line utility to interact with the project.  
settings.py – Project-level configuration (database, middleware, installed apps, etc.).  
urls.py – Main URL routing configuration.  
wsgi.py / asgi.py – Used for deployment (WSGI for traditional servers, ASGI for async support).  


### python manage.py startapp app_name  

This command creates a new Django app inside an existing project.
An app is a module that handles a specific feature or functionality (e.g., blog, authentication, payments).
```
python manage.py startapp blog
```

### Important Files:

models.py – Defines database models (tables).
views.py – Contains business logic and request handling.
admin.py – Registers models for Django admin panel.
apps.py – App configuration.
tests.py – For writing test cases.

⚠️ After creating an app, you must register it in settings.py under:

```
INSTALLED_APPS = [
    'blog',
]
```

### simple analogy

Project = Entire website/application  
App = A specific feature of that website  

start the Django development server  
1. run your project  
2. does not create anything  
python .\myfirstsite\manage.py runserver  

*** Normal Analogy  
startproject -- Create the city  
startapp --Create a building  
runserver --open the city so people can visit.  

Project Structure Details  
myfirstsite/myfirstsite/ (inner folder)  
--it does not contain the business logic-it contains setting and wiring.  

## ⚙️ Django Settings File

> The main configuration file of the Django project.

### Responsibilities

- **Installed Apps** – Registers applications used in the project  
- **Database Configuration** – Defines database connection settings  
- **Middleware** – Controls request and response processing  
- **Templates** – Manages template engine settings  
- **Static Files** – Configures CSS, JS, and image handling  
- **Security Settings** – Handles authentication and security policies

	
urls.py  
URL routing(URL->View Mapping)  

*** wsgi.py(sync)  
web server gateway interface  
	1.deploying django on server like Gunicorn,uWSGI  
	2.production environment  
	
*** asgi.py  
Asyncronous server gateway interface.  
used for:  
	Websockets  
	Async views  
	real-time apps(chat,notification)  
	(Daphne,Uvicorn)  

*** views.py  
Business Logic  
--Request are handled.  
--Responses are returned.   

*** tests.py    
--Automation testing  
	1.unit tests  
	2.integration tests  
	
*** Templates folder(django does not  create it automatically)    
## Templates Folder Structure

```
templates/
└── myapps/
    └── index.html
```

	
Static folder (Does not create by Django)
```
static/
│
└── myapps/
    ├── css/
    ├── js/
    └── images/
```

		
*** configured in setting.py  
