from django.db import models
import os
# Create your models here.


def user_directory_path():
    base_dir=((os.getcwd())+"/uploads/")
    return base_dir

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

