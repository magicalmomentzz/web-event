from email.policy import default
from django.db import models

# Create your models here.
class eventRegisterForm(models.Model):
    user_id = models.AutoField
    name = models.CharField(max_length=111)
    email = models.EmailField(max_length=111)
    mobNo = models.CharField(max_length=111)
    amount = models.CharField(max_length=111)
   