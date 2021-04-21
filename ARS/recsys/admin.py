from django.contrib import admin
from .models import User_Detail
from .models import Article
from .models import User_Search
from import_export.admin import ImportExportModelAdmin

@admin.register(Article)
class ArticleAdmin(ImportExportModelAdmin):
    pass
admin.site.register(User_Detail)
admin.site.register(User_Search)
# Register your models here.

