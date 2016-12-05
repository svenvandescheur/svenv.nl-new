from cms.toolbar_pool import toolbar_pool
from cms.extensions.toolbar import ExtensionToolbar
from django.utils.translation import ugettext_lazy as _
from .models import ArticleExtension


@toolbar_pool.register
class ArticleExtensionToolbar(ExtensionToolbar):
    """
    The toolbar for configuring an article (blog post).
    """
    model = ArticleExtension

    def populate(self):
        current_page_menu = self._setup_extension_toolbar()

        if current_page_menu:
            page_extension, url = self.get_page_extension_admin()

            if url:
                current_page_menu.add_modal_item(_('Article'),
                    url=url,
                    disabled=not self.toolbar.edit_mode)
