This is the capstone project for Meta Backend Developer Professional Certification.

Before testing, do create a virtual env, install the requirement.
The api paths that are to be tested  are:
/restaurant/menu/
/restaurant/booking/

To test the second path with insomnia will be difficult because of the default router class for the view in project urls.py file.
This was done as per the requirement in the exercise.
Nonetheless, you can test it by creating a superuser: python manage.py createsuperuser,
Give your own credentials.
The one used by me is username:admin, password:littlelemon123!

And the database is local.

For testing the models and views run : python manage.py test
