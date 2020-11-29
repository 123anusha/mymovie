from django.db import models
from django.contrib.auth.models import (
        BaseUserManager, AbstractBaseUser
)

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, name, email, password):
        if not email:
            raise ValueError('user must have an email address')
        user = self.model(email=self.model.normalize_email(email), name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(verbose_name='UserEmail', unique=True)
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    objects = UserManager()

    @property
    def is_active(self):
        return self.active

    @property
    def is_admin(self):
        return self.is_admin

    #def has_perm(self, perm, obj=None):
        #return True

    #def has_module_perm(self, app_label):
        #return True
