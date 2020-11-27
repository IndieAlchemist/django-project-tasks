from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils.translation import gettext_lazy as _

# Create your models here.

class CustomUser(AbstractUser):
    
    class Status(models.TextChoices):
        NEW = 'NEW', _('New')
        ACTIVE = 'ACTIVE',_('Active')
        SUSPENDED= 'SUSPENDED',_('Suspended')
        ARCHIVED = 'ARCHIVED',_('Archived')

    status=models.CharField(max_length=20,choices=Status.choices,default=Status.NEW) 