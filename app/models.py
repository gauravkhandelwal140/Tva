from django.db import models
from django.utils.translation import ugettext_lazy as _
from  django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    username = None
    dob = models.DateField(verbose_name=_('Date of Birth'), blank=True, null=True)
    # mobile = models.CharField(verbose_name=_('Mobile Number'), max_length=100, unique=True )
    email = models.EmailField(_('email address'), unique=True)
    company_name = models.CharField(verbose_name=_('Company Name'),max_length=200,blank=True, null=True)
    age=models.CharField(verbose_name=_('Age'), blank=True,max_length=200, null=True)
    city=models.CharField(verbose_name=_('City'), blank=True, max_length=200,null=True)
    state=models.CharField(verbose_name=_('State'), blank=True, max_length=200,null=True)
    zip = models.CharField(verbose_name=_('Zip Code'), blank=True, max_length=200,null=True)
    web = models.CharField(verbose_name=_('web'), blank=True, max_length=200,null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):
        return str(self.email)

