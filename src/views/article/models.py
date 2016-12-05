from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool
from django.db import models
from django.utils.translation import ugettext as _
from filer.fields.image import FilerImageField


class ArticleExtension(PageExtension):
    """
    A generic blog post with an optional comment section.
    """
    image = FilerImageField(verbose_name=_("image"))
    comments = models.BooleanField(_('comments'), default=True)


extension_pool.register(ArticleExtension)
