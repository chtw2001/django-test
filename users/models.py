from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class User_manager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError('이메일은 필수 값입니다.')
        
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password) # db에 password를 hashing 처리를 하여 저장 법적으로 정해진것
        user.save(using=self.db) # db에 저장
        return user
    
    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)
    
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, email, password, **extra_fields) 
        
        
# db로 쿼리를 날릴 때 제공해주는 인터페이스(커맨드 라인에서) => usermanager
class User(AbstractUser):
    name = models.CharField(verbose_name = '이름', max_length=10)
    
    objects = User_manager()
    
# class UserInfo(models.Model):
#     age = models.IntegerField(verbose_name = '나이')
#     user = models.ForeignKey(to = 'User', on_delete=models.CASCADE)