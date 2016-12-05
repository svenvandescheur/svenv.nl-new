from django.contrib import admin
from cms.extensions import PageExtensionAdmin

from .models import CategoryExtension


class CategoryExtensionAdmin(PageExtensionAdmin):
    """
    A recursive overview of all child articles.
    """
    pass

admin.site.register(CategoryExtension, CategoryExtensionAdmin)
