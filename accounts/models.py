from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)
class UserManager(BaseUserManager):
    def create_user(self, email, password, staff=False, admin=False, active=True):
        if not email:
            raise ValueError('이메일을 입력해주세요!')
        if not password:
            raise ValueError('비밀번호를 입력해주세요!')
        user = self.model(
            email = self.normalize_email(email),
        )
        user.set_password(password) # 유저의 비밀번호 설정(받아온 매개변수)
        user.staff = staff
        user.admin = admin
        user.active = active
        user.save(using=self._db)   # 설정된 데이터베이스(DB)에 user객체 저장
        return user                 # User Model에 user(객체)를 넘김
        
    def create_staffuser(self, email, password):
        user = self.create_user(
            email,
            password,
            staff = True
        )
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password,
            staff = True,
            admin = True
        )
        return user

class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique = True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True) # 로그인 할 수 있나?(휴면계정이 아닌가?)
    staff = models.BooleanField(default=False) # superuser가 아닌 staff(김현준, 주영민이 아니라 정택원)
    admin = models.BooleanField(default=False) # superuser(김현준, 주영민)
    
    USERNAME_FIELD = 'email' # 로그인시 username대신 email을 사용하겠다!
    REQUIRED_FIELDS = [] # python manage.py createsuperuser를 할 때 필요한 것

    objects = UserManager() # User.objects.create_user(email='ex@ex.ex' ...)로 쿼리를 만들어서 
                            # 유저를 만들어줌

    def __str__(self):
        return self.email
    
    @property # 나중에 사용할 때 User.is_staff() 가 아닌 => User.is_staff라고만 사용하여 가독성을 높여줌
    def is_staff(self):
        return self.staff
    
    @property
    def is_superuser(self):
        return self.admin

    def has_perm(self, perm, obj=None):
       return self.admin

    def has_module_perms(self, app_label):
       return self.admin
   