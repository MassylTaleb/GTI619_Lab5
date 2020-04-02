from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from enum import Enum
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User


class Roles(Enum):
    ADMIN = "Administrateur"
    CR = "Proposé aux clients résidentiels"
    CA = "Proposé aux clients clients d'affaire"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    isEmailConfirmed = models.BooleanField(default=False)
    role = models.CharField(max_length=37, choices=[(tag.value, tag.value) for tag in Roles])


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

def create_user_profile(sender, instance, created, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)

class Params(models.Model):
	isPeriodicChange = models.BooleanField(default=False)
	passMinLength = models.PositiveIntegerField(default=8)
	passMaxLength = models.PositiveIntegerField(blank=True, null=True)
	needUppercase = models.BooleanField(default=False)
	needLowercase = models.BooleanField(default=False)
	needSpecialChar = models.BooleanField(default=False)
	needNumericChar = models.BooleanField(default=False)
	cannotUsePreviousPass = models.BooleanField(default=False)
	numberOfAttemps = models.PositiveIntegerField(default=3)
	delayBetweenAttemps = models.PositiveIntegerField(default=1)
	contactAdminAfterFailure = models.BooleanField(default=False)

class GridCard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    key1 =  models.CharField(max_length=2)
    key2 =  models.CharField(max_length=2)
    key3 =  models.CharField(max_length=2)
    value1 =  models.CharField(max_length=1)
    value2 =  models.CharField(max_length=1)
    value3 =  models.CharField(max_length=1)
    active = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def update_user_gridcard(sender, instance, created, **kwargs):
    if created:
        GridCard.objects.create(user=instance)
    instance.gridcard.save()

def create_user_gridcard(sender, instance, created, **kwargs):
    try:
        instance.gridcard.save()
    except ObjectDoesNotExist:
        GridCard.objects.create(user=instance)