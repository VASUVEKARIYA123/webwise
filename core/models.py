from django.db import models
from django.contrib.auth.models import User

# User Profile Model
class AddressAndInfo(models.Model):
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    home_street = models.CharField(max_length=120)
    postal_code = models.CharField(max_length=6)
    phone = models.CharField(max_length=20)
    user = models.OneToOneField(to=User, unique=True, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user}'


class Profile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    info = models.OneToOneField(to=AddressAndInfo, on_delete=models.CASCADE, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, null=True)
    def __str__(self):
        return f'{self.first_name}'

    # def save(self, *args, **kwargs):
    #     self.user = self.request.user
    #     super(Profile, self).save(*args, **kwargs)
