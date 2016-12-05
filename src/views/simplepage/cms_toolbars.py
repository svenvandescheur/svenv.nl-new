from cms.toolbar_pool import toolbar_pool
from cms.extensions.toolbar import ExtensionToolbar
from django.utils.translation import ugettext_lazy as _
from .models import SimplePageExtension


@toolbar_pool.register
class SimplePageExtensionToolbar(ExtensionToolbar):
    """
    The toolbar for configuring a page.
    """
    model = SimplePageExtension

    def populate(self):
        current_page_menu = self._setup_extension_toolbar()

        if current_page_menu:
            page_extension, url = self.get_page_extension_admin()

            if url:
                current_page_menu.add_modal_item(_('Page'),
                    url=url,
                    disabled=not self.toolbar.edit_mode)
