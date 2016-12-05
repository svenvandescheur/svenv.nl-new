from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext as _


class CodeSnippetPlugin(CMSPlugin):
    """
    A simple CodeSnippet plugin allowing custom CSS classes.
    """
    code = models.TextField(_('Code'))
