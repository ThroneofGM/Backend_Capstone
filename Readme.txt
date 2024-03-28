This is the capstone project for Meta Backend Developer Professional Certification.

Before testing, do create a virtual env, install the requirement in the virtual env by running-
pip install django
pip install mysqlclient
pip install djangorestframework
pip install djoser

pardon the inconvenience, as I used python -m venv to create the virtual env which does not create the pipfile.

The database is local so change in settings.py according to your local database settings.
After that run the following commands:
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

The api paths that are to be tested  are:
/restaurant/menu/
/restaurant/booking/

To test the second path with insomnia will be difficult because of the default router class for the view in project urls.py file.
This was done as per the requirement in the exercise.
Nonetheless, you can test it by creating a superuser: python manage.py createsuperuser,
Give your own credentials.
The one used by me is username:admin, password:littlelemon123!

For testing the models and views run : python manage.py test
