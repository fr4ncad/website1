from django.db import models

import random
class user(models.Model):
    nev=models.CharField(max_length=20)
    jelszo=models.CharField(max_length=20)
    anonymus=models.IntegerField()
    access_level=models.CharField(max_length=1)
    def form(POST):
        if user.objects.filter(nev = POST['name'], jelszo = POST['password']):
            return True
        else:
            return False
    def __str__(self):
        return self.nev

class story(models.Model):
    title=models.CharField(max_length=40)
    author=models.CharField(max_length=9)
    access_level=models.CharField(max_length=1)
    content=models.CharField(max_length=100000)