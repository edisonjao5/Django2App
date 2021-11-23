from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from sorl.thumbnail import ImageField

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    SOCIAL = (
        ('twitter', 'Twitter'),
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('youtube', 'Youtube'),
        ('github', 'Github'),
    )
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Username = models.CharField(max_length=30)
    image = ImageField(upload_to='profiles')
    Password = models.CharField(max_length=30)
    Social = models.CharField(max_length=30, choices=SOCIAL)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, **kwargs):
    instance.profile.save()
