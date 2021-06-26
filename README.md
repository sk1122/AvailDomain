# AvailDomain - Search Domain Names

It checks if Entered Domain is available and also checks other domains similar to it is available . It uses `whois` python package to check domains.

## Project Structure

```
AvailDomain
├── AvailDomain
│   ├── __init__.py   
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── README.md
├── accounts
│   ├── __init__.py      
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── templates
│   │   ├── base.html
│   │   └── registration
│   │       ├── login.html
│   │       └── register.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── api
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-38.pyc
│   │       └── __init__.cpython-38.pyc
│   ├── models.py
│   ├── serializers.py
│   ├── template_views.py
│   ├── templates
│   │   ├── base.html
│   │   ├── check_domain.html
│   │   ├── history.html
│   │   └── profile.html
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
├── db.sqlite3
├── manage.py
└── static
    ├── bootstrap.min.css
    ├── check_domain.js
    └── js
```

### Authentication and Authorization
`accounts` is where all authentication and authorization happens.
- It uses inbuilt `Django Authentication System` with `Django Rest Framework` inbuilt `SessionAuthentication` and `BasicAuthentication`.

### Rest API with Templates
`api` is where all main logic of application happens.
- It uses `whois` package for getting details of entered domains.
- `views` includes rest api's developed using Django Rest Framework.
- `template_views` includes templates.
- `utils` includes utility function which uses `whois` package

## Routes

### Rest API
```
/api/check_domain - Gets Details about Domain.
/api/check_domain2 - Checks if other domains are available similar to entered domain
(There are 2 routes because we have to store history of users activity. So if it requests first route then it is stored in history otherwise not)
/api/get_available_tlds - Returns Available TLD's (.com, .in...)
/api/get_history - Returns History of Logged In User
```

### Templates
```
/ - Enter Domain and Get Details
/profile - Profile Of User with his/her History.
```

### Authentication
```
/accounts/register - Register Route
/accounts/login - Login Route
/accounts/logout - Logout Route
```

## Run App Locally

- Create a Virtual Enviornment with `venv` or `virtualenv`
- Activate Virtual Env and run this command to install dependencies
```
pip install -r requirements.txt
``` 
- Then Create Migrations `python3 manage.py makemigrations`
- Run Migrations `python3 manage.py migrate`
- Run App `python3 manage.py runserver`

