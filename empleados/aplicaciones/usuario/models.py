"""
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"Usuario: {self.user}"
    """

from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin, UserManager, Group, Permission
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, email, password, **extra_fields):
        #Creates and saves a User with the given email and password
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_staff', True)
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        
        return self._create_user(email, password, **extra_fields)
    
class User (AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Email address', unique=True, max_length=100, null=False)
    password = models.CharField('Password', max_length=100, unique=False)
    username = models.CharField('Username', max_length=30, blank=True)
    nombre = models.CharField('Nombre', max_length=20, blank=True, null=True)
    apellido = models.CharField('Apellido', max_length=20, blank=True, null=True)
    is_staff = models.BooleanField('Staff', default=False)
    is_superuser = models.BooleanField('Superuser', default=True)
    is_admin = models.BooleanField('Admin', default=False)
    is_active = models.BooleanField('Active', default=True)
    date_joined = models.DateTimeField(('date joined'),auto_now_add=True)
    objects = UserManager()
    groups = models.ManyToManyField(Group, verbose_name=_('groups'), related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, verbose_name=_('user permissions'), related_name='custom_user_set')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido']
    
    class Meta:
        verbose_name = ('User')
        verbose_name_plural = ('Users')
        
    def get_full_name(self):
        #Returns the first name and the last name with a space in between
        full_name = '%s %s' % (self.nombre, self.apellido)
        return full_name.strip()
    
    def get_short_name(self):
        #Returns the short name
        return self.nombre
    
    def email_user(self, subject, message, from_email=None, **kwargs):
        #Sends an email to this user
        send_mail(subject, message, from_email, [self.email], **kwargs)

