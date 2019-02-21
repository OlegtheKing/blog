from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)  # whenever object is created is sends signal to receiver which takes it
def create_profile(sender, instance, created, **kwargs):  # and calls following function with all arguments from sender
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()