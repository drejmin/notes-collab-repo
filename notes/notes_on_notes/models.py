from django.db import models
from datetime import date

# Create your models here.
class Note(models.Model):
    title= models.CharField(max_length=30)
    content= models.TextField(max_length= 500)
    date_created = date.today() 
    last_modified= date.today()