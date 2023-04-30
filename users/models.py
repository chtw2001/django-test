# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# class UserManager(BaseUserManager):

#     def create_user(self, id, email, name, password=None):
#         if not email:
#             raise ValueError('must have user email')
#         if not name:
#             raise ValueError('must have user name')
        
#         user = self.model(
#             email = self.normalize_email(email),
#             name = name,
#             id = id,
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self,id, email, name, password=None):
#         user = self.create_user(
#             email = email,
#             password = password,
#             name = name,
#             id = id
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user

# class User(AbstractBaseUser):
#     id = models.AutoField(primary_key=True)
#     email = models.EmailField(default='', max_length=100, null=False, blank=False, unique=True)
#     name = models.CharField(default='', max_length=100, null=False, blank=False)

#     # User 모델의 필수 field
#     is_active = models.BooleanField(default=True)    
#     is_admin = models.BooleanField(default=False)
    
#     objects = UserManager()
    
#     @property
#     def is_superuser(self):
#         return self.is_admin

#     @property
#     def is_staff(self):
#        return self.is_admin

#     def has_perm(self, perm, obj=None):
#        return self.is_admin

#     def has_module_perms(self, app_label):
#        return self.is_admin

#     @is_staff.setter
#     def is_staff(self, value):
#         self._is_staff = value
    
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['id', 'name']

#     def __str__(self):
#         return self.name

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