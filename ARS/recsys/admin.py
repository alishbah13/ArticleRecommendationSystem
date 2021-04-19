from django.contrib import admin
from .models import User
from .models import Article
from .models import User_Search

admin.site.register(User)
admin.site.register(Article)
admin.site.register(User_Search)
# Register your models here.
