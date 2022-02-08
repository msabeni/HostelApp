from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField

# Create your models here.
class User (AbstractUser):
    is_matron = models.BooleanField('matron status',default = False) 
    is_student = models.BooleanField('student status',default = False) 
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def save_user (self) :
        self.save()
    def update_user (self) :
        self.update()
    def delete_user (self) :
        self.delete()
    
class Matron (models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE , primary_key=True,)
    profile_pic = CloudinaryField ('image')
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length= 13)

    def __str__(self):
        return f'{self.user}'

    def save_matron (self) :
        self.save()
    def update_matron (self) :
        self.update()
    def delete_matron (self) :
        self.delete()

class Student (models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE , primary_key=True)
    profile_pic = CloudinaryField ('image')
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length= 13)
    registration_no = models.CharField (max_length=20)

    def __str__(self):
        return f'{self.user}'

    def save_student (self) :
        self.save()
    def update_student (self) :
        self.update()
    def delete_student (self) :
        self.delete()

class Profile (models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)
    profile_pic = CloudinaryField ('image')
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length= 13)
    bio = models.TextField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} profile'
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
            if created:
                Profile.objects.create(bio=instance)

    @receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
    def save_user_profile(sender, instance, created, **kwargs):
            user = instance
            if created:
                profile = Profile(user=user)
                profile.save()


