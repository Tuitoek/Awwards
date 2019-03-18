# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    link = models.CharField(max_length=1000)
    landingpic = models.ImageField(upload_to='images')

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

class Profile(models.Model):
    dpicture = models.ImageField(upload_to='dp')
    bio = models.CharField(max_length=50)
    projectsposted = models.ForeignKey(Project)
    contacts = models.CharField(max_length=12,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_bio(self,bio):
        self.bio = bio
        self.save()
