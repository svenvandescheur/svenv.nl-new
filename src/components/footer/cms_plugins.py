from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _


class FooterPlugin(CMSPluginBase):
    """
    A simple navigation bar plugin.
    """
    module = _('Website elements')
    name = _('Footer')
    render_template = "footer_plugin.html"


plugin_pool.register_plugin(FooterPlugin)
