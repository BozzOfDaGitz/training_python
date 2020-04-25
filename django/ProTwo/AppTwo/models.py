from django.db import models

# Create your models here.
class User(models.Model):

    first_name = models.CharField(max_length=24)
    last_name = models.CharField(max_length=24)
    e_mail = models.EmailField(unique=True)

    def __str__(self):
        return '{} {} ({})'.format(self.first_name,self.last_name,self.e_mail)
