from django.db import models


class Contact(models.Model):
        name = models.CharField(max_length=100)
        email = models.CharField(max_length=100)
        textarea = models.CharField(max_length=100)
        date = models.DateField()
        
class users(models.Model):
        name = models.CharField(max_length=100)
        email = models.CharField(max_length=100)
        password = models.CharField(max_length=100)
        
