from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from django.urls import reverse


class OrchesterToolbar(CMSToolbar):
    def populate(self):
        menu = self.toolbar.get_or_create_menu(
            key='orchester_cms_integration',
            verbose_name='Orchester'
        )
        menu.add_break(identifier='settings_section')
        menu.add_sideframe_item(  # or add_button(), add_modal_item(), etc
            name='Admin panel',
            url=reverse('orchester:index')
        )


toolbar_pool.register(OrchesterToolbar)
