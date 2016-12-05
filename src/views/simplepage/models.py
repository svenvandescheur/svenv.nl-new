from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool
from django.utils.translation import ugettext as _
from filer.fields.image import FilerImageField


class SimplePageExtension(PageExtension):
    """
    A generic website page.
    """
    image = FilerImageField(verbose_name=_("image"))


extension_pool.register(SimplePageExtension)
