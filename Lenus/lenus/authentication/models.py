from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE, primary_key= True,related_name='users')
    first_name= models.CharField(max_length=100,null=True)
    last_name= models.CharField(max_length=100,null=True)
    email= models.CharField(max_length=100,null=True)
    DOCTOR = 'DOC'
    FIRESERVICE = 'FRS'
    POLICE = 'POL'
    VOLUNTEER = 'VTR'
    PHYSIOTHERAPIST = 'PHY'
    PROFESSION_CHOICES = [
        (DOCTOR, 'Doctor'),
        (FIRESERVICE, 'Fire Service'),
        (POLICE, 'Police'),
        (VOLUNTEER, 'Volunteer'),
        (PHYSIOTHERAPIST, 'Physiotherapist'),
    ]
    profession = models.CharField(
        max_length=15,
        choices=PROFESSION_CHOICES,
        default=VOLUNTEER,
        null=True,
    )
    profile_pic=models.ImageField(upload_to='profile_pics', null=True, blank= True)
    location= models.CharField(max_length=100,null=True,blank=True,default="")
    phone=models.IntegerField(null=True,blank=True,default=0)
    USERNAME_FIELD = 'username'


    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile=UserProfile.objects.create(user=kwargs['instance'])


    post_save.connect(create_profile,sender=User)
