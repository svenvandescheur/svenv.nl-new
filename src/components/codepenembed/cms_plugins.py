from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import CodepenEmbedPlugin


class CodepenEmbedPlugin(CMSPluginBase):
    """
    An embedded code pen.
    """
    model = CodepenEmbedPlugin
    module = _("Generic")
    name = _('Codepen embed')
    render_template = "codepen_embed_plugin.html"


plugin_pool.register_plugin(CodepenEmbedPlugin)
