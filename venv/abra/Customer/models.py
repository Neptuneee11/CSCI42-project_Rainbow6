from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    #first_name = models.CharField(max_length=100, blank=False)
    #last_name = models.CharField(max_length=100, blank=False)
    #email = models.EmailField(max_length=100, blank=False)
    id_number = models.IntegerField(blank=False, validators=[MinValueValidator(100000), MaxValueValidator(999999)])
    school_year = models.CharField(max_length=20, blank=False)
    course = models.CharField(max_length=50, blank=False)
    phone_number = models.IntegerField(blank=False, validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)])

    def __str__(self):
        return self.user.username
    
#automatically make a profile when customer registers
'''def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile(user=instance)
        user_profile.save()

#automation
post_save.connect(create_profile, sender=User)'''
