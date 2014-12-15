from django.utils.translation import ugettext as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import *

class MenuBelowThisPlugin(CMSPluginBase):
    """
    Model for menu below current page.
    """
    model = MenuBelowThisModel
    name = _("Menu Below This")
    render_template = "amenu/menu_below_this.html"

    def render(self, context, instance, placeholder):
        context.update({'i' : instance})
        return context

plugin_pool.register_plugin(MenuBelowThisPlugin)
