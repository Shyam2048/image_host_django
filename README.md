# image_host_django
Allows a user to upload and see images using authentication


1- For the database I have used Postgresql . So, Download the postgresql first and make changes in the settings.py in imageshost.
   It should look like this:
   'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'imagehost',
            'USER': 'postgres',
            'PASSWORD': 'dhdhdgh',
            'HOST': 'localhost',
            'PORT': 5432,
            }
2-  uploads folder stores the images of each user
3- You need to makemigrations first by running py manage.py makemigrations and then py manage.py migrate
