from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
	user			  = models.OneToOneField(User)
	activated 		  = models.BooleanField(default=False)
	timestamp		  = models.DateTimeField(auto_now_add=True)
	updated 		  = models.DateTimeField(auto_now=True)
	email_confirmed   = models.BooleanField(default=False)
	birth_date        = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()