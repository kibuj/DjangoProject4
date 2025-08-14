from django.conf import settings
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True, upload_to='users/%Y/%m/%d')

    def __str__(self):
        return str(self.user)
