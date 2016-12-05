from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import ImagePlugin


class ImagePlugin(CMSPluginBase):
    """
    A simple image plugin allowing custom CSS classes.
    """
    model = ImagePlugin
    module = _("Generic")
    name = _('Image')
    render_template = "image_plugin.html"


plugin_pool.register_plugin(ImagePlugin)
