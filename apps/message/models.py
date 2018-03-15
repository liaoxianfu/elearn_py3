from django.db import models

from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    nick_name=models.CharField(
        max_length=50,
        verbose_name=u'昵称',
        default='',
        birthday=models.DateTimeField(
            verbose_name=u'生日'
        )
    )

