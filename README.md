# image_host_django
Allows a user to upload and see images using authentication


For the database I have used Postgresql . So, Download the postgresql first and make changes in the settings.py in imageshost.
It should look like this:
'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'imagehost',
            'USER': 'postgres',
            'PASSWORD': 'dhdhdgh',
            'HOST': 'localhost',
            'PORT': 5432,
            }
