from django.db import models
from cms.models import CMSPlugin
from cms.models.pagemodel import Page
from cms.models.fields import PageField

class MenuBelowThisModel(CMSPlugin):
    """
    Menu plugin for DjangoCMS.
    """
    depth = models.PositiveIntegerField(max_length = 3, default = 1, help_text = "Depth from current menu.")
    template = models.CharField(max_length = 50, null = True, blank = True, help_text = "Path to the template for this menu. e.g. 'amenu/template_name.html'")
    display_menu_heading = models.BooleanField(default = 1)


class BreadcrumbModel(CMSPlugin):
    """
    Model for Breadcrumb.
    """
    start_level = models.PositiveIntegerField(default = 0, help_text = "Level from where this breadcrumb will start. 0 = root level")
    template = models.CharField(max_length = 50, null = True, blank = True, help_text = "Path to the template for this menu. e.g. 'amenu/template_name.html'")


class GenericMenuModel(CMSPlugin):
    """
    Model for generic menu. Makes use of 'show_menu' cms tag.
    """
    start_level = models.PositiveIntegerField(default = 0, help_text = "Level at which menu should start.")
    end_level = models.PositiveIntegerField(default = 100, help_text = "Level at which menu should end.")
    extra_inactive = models.PositiveIntegerField(default = 100, help_text = "Level of navigation to be displayed if a node is not a direct ancestor or decendent of the current active node. 0 is root level.")
    extra_active = models.PositiveIntegerField(default = 100, help_text = "Level of descendants of the currently active node to be displayed.")
    template = models.CharField(max_length = 50, null = True, blank = True, help_text = "Path to the template for this menu. e.g. 'amenu/template_name.html'")


class SelectiveMenuModel(CMSPlugin):
    """
    Model for selective menu.
    """
    page = PageField()
    depth = models.PositiveIntegerField(default = 1)
    display_menu_heading = models.BooleanField(default = 1)
