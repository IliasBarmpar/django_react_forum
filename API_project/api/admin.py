from django.contrib import admin
from .models import Article

# Alternative 1
# admin.site.register(Article)


# Alternative 2
@admin.register(Article)
class ArticleModel(admin.ModelAdmin):
    list_filter = ('title', 'description')
    list_display = ('title', 'description')
