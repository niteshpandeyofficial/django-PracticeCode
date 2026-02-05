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

*** setting.py  
The brain of Django project  
This file control  
	1.Installed apps  
	2.Database configuration  
	3.Middleware  
	4.Templates  
	5.Static Files  
	6.Security Settings  
	
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
Fromtend presentation layer.  
Structure  
	templates/  
		myapps/  
			insex.html  
	
*** Static folder(Does not create by Django)  
static/  
	myapps/  
		css/  
		js/  
		images/  
		
*** configured in setting.py  
