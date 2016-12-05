from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import CodeSnippetPlugin


class CodeSnippetPlugin(CMSPluginBase):
    """
    A simple CodeSnippet plugin allowing custom CSS classes.
    """
    model = CodeSnippetPlugin
    module = _("Generic")
    name = _('Code snippet')
    render_template = "code_snippet_plugin.html"


plugin_pool.register_plugin(CodeSnippetPlugin)
