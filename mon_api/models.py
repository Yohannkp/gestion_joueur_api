from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission
from django.utils.translation import gettext_lazy as _

class Personne(AbstractUser):
    age = models.PositiveIntegerField()
    mail = models.EmailField()

    USERNAME_FIELD = 'username'

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=_('groups'),
        blank=True,
        related_name='mon_api_personnes',
        related_query_name='mon_api_personne',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=_('user permissions'),
        blank=True,
        related_name='mon_api_personnes',
        related_query_name='mon_api_personne',
    )

class Player(Personne):
    score = models.IntegerField()
    credits = models.IntegerField()

class Manager(Personne):
    department = models.CharField(max_length=100)