# Responsive API

### Responsive Fullstack CRUD System
#### Features
✅Login System<br>
✅Responsive Template<br>
✅Bootstrap4 Template Integration<br>
✅Anti-CSRF Security<br>
✅PostgreSQL Integration<br>
✅Django ORM Integration<br>
✅Pagination<br>
✅Session Auth<br>
✅Filter by Post Authors<br>
✅Authors List<br>
✅PEP8 Good Practices using Flake8 as code linter<br>
✅Read Only mode for non-authenticated Users<br>
✅OOP Code Based<br>
✅Django-admin Interface<br>

## Endpoints
```
http://127.0.0.1:8000/ - Homepage List
http://127.0.0.1:8000/<str:author> - Author Post list
http://127.0.0.1:8000/posts/ - Post list
http://127.0.0.1:8000/posts/<str: author>/ - Post list from author
http://127.0.0.1:8000/posts/<int:id>/ - Post detail page
http://127.0.0.1:8000/posts/<int:id>/ - Post detail page
http://127.0.0.1:8000/posts/create/ - Form Based Post Creation
http://127.0.0.1:8000/posts/delete/ - Post Deletion with deletion confirm form
http://127.0.0.1:8000/posts/update/ - Form Based Post Update
```
## Port
```
Default port is 8000, but can be changed on server run (Description below).
```

## Params
| Name   |      Type      |  Description | Required
|:----------:|:-------------:|:----------:|:------:|
| Id |  Int | Id of desired Post | No
| author |  String | author username | No


## How to use

### Clone the repository
```
git clone https://github.com/gustavopirro/ResponsiveCrud.git
```
### Enter the project folder
```
cd path/of/project
```

### Create virtual enviroment
```
python -m venv venv
```

### Activate virtual enviroment
```
venv/scripts/activate
```

### Download and install dependencies
```
pip install -r requirements.txt
```

### Create '.env' file inside ResponsiveCrud root folder, in the same directory as manage.py.
```
|---Root
|---manage.py
|---responsivecrud
|------settings.py
|------local_settings.py
```

### Generate a new secret key, you can use the site below:
[https://djecrety.ir/](https://djecrety.ir/)

## PostgreSQL Configuration
### With postgreSQL installed in your local machine, add the code bellow in your local_settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_name',
        'HOST': 'db_host',
        'PORT': 'db_port',
        'USER': 'db_user',
        'PASSWORD': 'db_password',
    }
}
```

### Change the fields db_name, db_host, db_port, db_user and db_password accordingly
example:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'HOST': 'localhost'
        'PORT': '5432',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
    }
}
```

### Don't forget to created a new db in your postgreSQL with the same name of your DB_NAME local_settings value

### With your terminal in the project root folder, run the following command:
```
python manage.py migrate # This will create the required tables inside your postgre database.
```

## Running the server
### Again in the project root folder, run the server with the command:
```
python manage.py runserver
```
### If you want to use a port other than 8000, run the command like this:
```
python manage.py runserver 127.0.0.1:desired_port
```
