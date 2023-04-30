from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(verbose_name = '이름', max_length=10, unique=True)
    
    
class UserInfo(models.Model):
    age = models.IntegerField(verbose_name = '나이')
    user = models.ForeignKey(to = 'User', on_delete=models.CASCADE)