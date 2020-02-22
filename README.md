### I'm gonna share Django Example codes here
# Wagtail DJANGO CMS

In this application you gonna find wagtail examples. In this situation db is sqlite3 but easily can change from mysite.settings.base.py
As you know in django applications database can change easily from config file.
## Installation

### Local

Create virtual environment and activate it

    virtualenv venv/
    source venv/bin/activate

Install requirements 

    pip install -r requirements.txt

make sure when you change your models you migrate your database.

    python manage.py makemigrations
    python manage.py migrate