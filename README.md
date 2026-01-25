# Django

WSGI is synchronous and best for traditional web apps, while ASGI is asynchronous and designed for real-time, high-concurrency applications like WebSockets and async APIs.
*** Django started with WSGI
1. Modern Django supports ASGI
2. You can still run Django in WSGI mode if:
3. No WebSockets
4. Simple APIs

Use ASGI if:
> WebSockets
>  Background tasks
> High concurrency

Steps to create first Web App
1. install django
```pip install django```

2. run below command
```django-admin startproject project_name```

3. run the server
```python .\myfirstsite\manage.py runserver```
