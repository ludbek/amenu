from django.utils.translation import ugettext as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import *

class AMenuPlugin(CMSPluginBase):
    module = "Menu"

class MenuBelowThisPlugin(AMenuPlugin):
    """
    Plugin for menu below current page.
    """
    model = MenuBelowThisModel
    name = _("Menu Below This")
    render_template = "amenu/menu_below_this.html"

    def render(self, context, instance, placeholder):
        context.update({'i' : instance})
        return context


class BreadcrumbPlugin(AMenuPlugin):
    """
    Plugin displays breadcrumb.
    """
    model = BreadcrumbModel
    name = _("Breadcrumb")
    render_template = "amenu/breadcrumb.html"

    def render(self, context, instance, placeholder):
        context.update({'i' : instance})
        return context

plugin_pool.register_plugin(MenuBelowThisPlugin)
plugin_pool.register_plugin(BreadcrumbPlugin)
