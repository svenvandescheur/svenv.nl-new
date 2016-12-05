from django.contrib import admin
from cms.extensions import PageExtensionAdmin

from .models import ArticleExtension


class ArticleExtensionAdmin(PageExtensionAdmin):
    """
    A generic blog post with an optional comment section.
    """
    pass

admin.site.register(ArticleExtension, ArticleExtensionAdmin)
