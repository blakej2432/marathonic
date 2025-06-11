from django.contrib.auth.models import AbstractUser
from django.db import models

from profiles.manager import CustomUserManager
from race.models import Race

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    race = models.ManyToManyField(
        Race,
        related_name="race_bookmark",
        blank=True,
        verbose_name="저장한대회"
        )
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"
    
    class Meta:
        db_table = "customuser"
        verbose_name = "사용자"
        verbose_name_plural = "사용자"