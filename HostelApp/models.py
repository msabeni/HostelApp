from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField

# Create your models here.
class User (AbstractUser):
    USERNAME_FIELD = 'username'
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

class Room (models.Model) :
    occupant = models.ForeignKey('Student', on_delete=models.CASCADE, null=True)
    in_charge = models.ForeignKey('Matron',on_delete=models.CASCADE,null=True)
    room_no = models.CharField(max_length=5)
    status = models.BooleanField(null=True)
    
    def __str__(self):
        return self.room_no
    def create_room(self):
        self.save()

    def update_room(self):
        self.save()

    def delete_room(self):
        self.delete()

    def find_room(cls,room_id):
        room = cls.objects.filter(room_id=room_id)
        return room

class Profile (models.Model) :
    GENDER_CHOICES = (
        (u'Male', u'Male'),
        (u'Female', u'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)
    profile_pic = CloudinaryField ('image')
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length= 13)
    bio = models.TextField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(null=True,max_length=15, choices=GENDER_CHOICES)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, related_name='room_owner', blank=True)

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

