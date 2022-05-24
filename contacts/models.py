from django.db import models
from django.contrib.auth.models import User

class Contacts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country_code = models.CharField(max_length=4)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    profile_picture = models.URLField(null=True)
    is_favorite = models.BooleanField(default=False)

   
    class Meta:
        verbose_name = "Contacts"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.user.username