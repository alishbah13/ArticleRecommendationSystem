from import_export import resources
from .models import Article

class ArticleResource(resources.ModelResource):
    class Meta:
        model = Article