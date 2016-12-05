from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext as _


LANGUAGE_CHOICES = (
    ('html', 'HTML'),
    ('css', 'CSS'),
    ('js', 'JavaScript'),
)


class CodepenEmbedPlugin(CMSPlugin):
    """
    An embedded code pen.
    """
    pen = models.CharField(_('Codepen identifier'), max_length=6)
    user = models.CharField(_('Codepen user'), max_length=255)
    height = models.IntegerField(_('Height'), default=480)
    selected_language = models.CharField(_('Language'), choices=LANGUAGE_CHOICES, max_length=10, blank=True, null=True)
    show_result = models.BooleanField(_('Show result'), default=True)
    theme_id = models.IntegerField(_('Theme id'), default=26505)


