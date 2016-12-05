from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _


class NavbarPlugin(CMSPluginBase):
    """
    A simple navigation bar plugin.
    """
    model = CMSPlugin
    module = _('Website elements')
    name = _('Navigation bar')
    render_template = "navbar_plugin.html"


plugin_pool.register_plugin(NavbarPlugin)
