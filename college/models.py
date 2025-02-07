from django.db import models

# Create your models here.

class Notice(models.Model):
    subject = models.CharField(max_length=100)
    msg = models.TextField() #message can be of any length
    cr_date = models.DateTimeField(auto_now_add=True) 
    #auto_now=True means it will take the current date and time when the notice is updated
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    
