from django.db import models
import uuid
from django.contrib.auth.models import User


class Userlogin(models.Model):
    user=models.ForeignKey(User, on_delete = models.CASCADE,null=True,blank=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username
