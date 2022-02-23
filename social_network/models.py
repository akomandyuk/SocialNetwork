from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.ManyToManyRel(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)
    first_name = models.TextField(blank=True)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=100, default='Male/Female')
    email = models.EmailField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="social_network/static/profile")


    def __str__(self):
        return self.user



class CreateTeam(models.Model):
    title = models.CharField(max_length=35)
    description = models.TextField(null=True, blank=True)
    logo = models.ImageField(null=True, blank=True, upload_to="social_network/static/teams")
    date_event = models.DateTimeField(auto_now_add=True)
    event_description = models.TextField(null=True, blank=True)
    members = models.IntegerField()
    sport = models.BooleanField(default=False)


    def __str__(self):
        return self.title


