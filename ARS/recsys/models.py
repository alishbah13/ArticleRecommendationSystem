from django.db import models
from django.contrib.auth.models import User


class User_Detail(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.OneToOneField(User, max_length=30, on_delete=models.CASCADE)
    # first_name = models.CharField(max_length=40)
    # last_name = models.CharField(max_length=40)
    # email = models.CharField(max_length=80)
    # password = models.CharField(max_length=20)
    dob = models.DateField()
    passport = models.CharField(max_length=20, unique=True)
    countryid = models.IntegerField()
    # approved = models.BooleanField()
    

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
    search_id = models.IntegerField(unique=True)
    query = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    results = models.TextField()
    username = models.ForeignKey(User_Detail, related_name='Searches', on_delete=models.RESTRICT)
    
    def _str_(self):
        return self.query, self.username