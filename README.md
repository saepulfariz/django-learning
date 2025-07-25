# DJANGO Learning

## Initial Setup

```bash
python -m venv venv or python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install django==4.2
pip install mssql-django
pip install django-mssql-backend  # Driver SQL Server untuk Django
pip install Pillow                # Untuk upload dan manipulasi gambar
django-admin startproject apps . #
```

## New App

```bash
python manage.py startapp products
```

## Register App

Add 'products', INSTALLED_APPS in settings.py.

## Migration database

```bash
python manage.py makemigrations products
python manage.py migrate
```

## Run project

```bash
python manage.py runserver
```

## Export Import Library

```bash
pip install -r requirements.txt
pip freeze > requirements.txt
```
