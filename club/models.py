from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.models import User
from PIL import Image
from tinymce.models import HTMLField
import os
# Create your models here.
class Club(models.Model):
    convener = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='club_logos/')
    moto = models.CharField(max_length=255)
    cover_picture = models.ImageField(upload_to='club_covers/')
    description = HTMLField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ClubMember(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    user = models.CharField(max_length=50) # club member = user
    position = models.CharField(max_length=100)
    email = models.EmailField()
    profile_picture = models.ImageField(upload_to='club_members/', null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.position} ({self.club.name})"


class ClubPost(models.Model):
    POST_TYPES = [
        ('announcement', 'Announcement'),
        ('event', 'Event Details'),
        ('other', 'Other'),
    ]

    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    posted_by = models.ForeignKey(ClubMember, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = HTMLField()
    post_type = models.CharField(max_length=20, choices=POST_TYPES)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    cover_photo = models.ImageField(upload_to='club_posts/', null=True, blank=True)
    pic1 = models.ImageField(upload_to='club_posts/', null=True, blank=True)
    pic2 = models.ImageField(upload_to='club_posts/', null=True, blank=True)
    pic3 = models.ImageField(upload_to='club_posts/', null=True, blank=True)
    pic4 = models.ImageField(upload_to='club_posts/', null=True, blank=True)
    pic5 = models.ImageField(upload_to='club_posts/', null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.club.name})"


