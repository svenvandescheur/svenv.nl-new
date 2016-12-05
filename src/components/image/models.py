from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext as _
from filer.fields.image import FilerImageField


class ImagePlugin(CMSPlugin):
    """
    A simple image plugin allowing custom CSS classes.
    """
    alt_text = models.CharField(_('Alternative text'), max_length=255)
    image = FilerImageField(verbose_name=_("image"))
    class_name = models.CharField(_('CSS class'), max_length=255, blank=True, null=True)
