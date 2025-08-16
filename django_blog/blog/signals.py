from django.db.models.signals import post_save
from django.dispatch import receiver   
from django.contrib.auth.models import User
from .models import Profile

# Automatically create or update the user profile when a User instance is created or updated
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()

# This signal handler ensures that a Profile instance is created when a User is created,
# and that the Profile instance is saved whenever the User instance is updated.
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save() 