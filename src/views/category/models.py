from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool
from django.db import models
from django.utils.translation import ugettext as _


class CategoryExtension(PageExtension):
    """
    A recursive overview of all child articles.
    """
    children_template_name = models.CharField(_('Children template name'), max_length=255, default='article')


extension_pool.register(CategoryExtension)
