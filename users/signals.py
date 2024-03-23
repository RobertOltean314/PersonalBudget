from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from budget.models import Budget
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # When a new User instance is created, create a corresponding Profile instance
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    # Save the associated Profile instance whenever a User instance is saved
    instance.profile.save()  # This line is causing an error. See what needs to be done.

@receiver(post_save, sender=User)
def create_budget(sender, instance, created, **kwargs):
    # When a new User instance is created, create a corresponding Budget instance
    if created:
        Budget.objects.create(user=instance)