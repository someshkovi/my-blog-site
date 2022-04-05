## Getting started
```bash
#clone the code 
$ git clone https://github.com/someshkovi/my-blog-site.git
$ cd djangoProject
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$ # Install modules - SQLite Storage
$ pip3 install -r requirements.txt
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
$
$ # Start the app - custom port
$ # python manage.py runserver 0.0.0.0:<your_port>
$
$ # Access the web app in browser: http://127.0.0.1:8000/
```

## code base structure
```bash
< PROJECT ROOT >
  |
  |--djangoProject/                   #global app configuration
  |--
```

## Deployment
### [Gunicorn](https://gunicorn.org/)
```bash
$ pip install gunicorn
```
> Start the app using gunicorn binary

```bash
$ gunicorn --bind=0.0.0.0:8001 core.wsgi:application
Serving on http://localhost:8001
```
Visit `http://localhost:8001` in your browser. The app should be up & running.

<br />
