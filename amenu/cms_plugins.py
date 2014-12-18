from django.utils.translation import ugettext as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pagemodel import Page
from django import forms
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


class GenericMenuPlugin(AMenuPlugin):
    """
    Plugin allows user to render menu at different level. It uses 'show_menu' cms tag.
    """
    model = GenericMenuModel
    name = _("Generic Menu")
    render_template = "amenu/generic_menu.html"

    def render(self, context, instance, placeholder):
        context.update({'i' : instance})
        return context


# class SelectiveMenuForm(forms.ModelForm):
#     pages = forms.MultipleChoiceField(choices = [(page.pk, "%s %s"%('--'*page.level, str(page))) for page in Page.objects.public()], widget = forms.CheckboxSelectMultiple)

#     class Meta:
#         model = SelectiveMenuModel


class SelectiveMenuPlugin(AMenuPlugin):
    """
    Plugin allows user to render selected menus.
    """
    model = SelectiveMenuModel
    name = _("Selective Menu")
    render_template = "amenu/selective_menu.html"
    # form = SelectiveMenuForm

    def render(self, context, instance, placeholder):
        context.update({'i' : instance})
        return context

plugin_pool.register_plugin(MenuBelowThisPlugin)
plugin_pool.register_plugin(BreadcrumbPlugin)
plugin_pool.register_plugin(GenericMenuPlugin)
plugin_pool.register_plugin(SelectiveMenuPlugin)
