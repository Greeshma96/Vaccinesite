from django.db import models

# Create your models here.
class Register(models.Model):
    username=models.CharField(max_length=50)
    first_name=models.CharField(max_length=50)
    password=models.CharField(max_length=8)

    def __str__(self):
        return self.username


