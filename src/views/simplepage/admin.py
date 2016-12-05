from django.contrib import admin
from cms.extensions import PageExtensionAdmin

from .models import SimplePageExtension


class SimplePageExtensionAdmin(PageExtensionAdmin):
    """
    A generic website page.
    """
    pass

admin.site.register(SimplePageExtension, SimplePageExtensionAdmin)
