from django.contrib import admin
from .models import User_Detail
from .models import Article
from .models import User_Search

admin.site.register(User_Detail)
admin.site.register(Article)
admin.site.register(User_Search)
# Register your models here.
