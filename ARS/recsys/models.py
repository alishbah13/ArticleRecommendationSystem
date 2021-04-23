from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class User_Detail(models.Model):
    username = models.OneToOneField(User, max_length=30, on_delete=models.CASCADE)
    dob = models.DateField()
    passport = models.CharField(max_length=20, unique=True)
    countryid = models.IntegerField()
    approved = models.BooleanField(default=False)
    

    def _str_(self):
        return self.username

class Article(models.Model):
    paper_id = models.IntegerField(unique=True)
    paper_title = models.CharField(max_length=100)
    author_keywords = models.TextField()
    abstract = models.TextField()
    area = models.CharField(max_length=100)

    def _str_(self):
        return self.paper_title

class User_Search(models.Model):
    query = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    results = models.TextField()
    username = models.CharField( max_length=30 )
    
    def _str_(self):
        return self.query, self.username