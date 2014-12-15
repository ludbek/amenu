from django.db import models
from cms.models import CMSPlugin

class MenuBelowThisModel(CMSPlugin):
    """
    Menu plugin for DjangoCMS.
    """
    depth = models.PositiveIntegerField(max_length = 3, default = 1)
    #start_level = None
    template = models.CharField(max_length = 50, null = True, blank = True)


class BreadcrumbModel(CMSPlugin):
    """
    Model for Breadcrumb.
    """
    start_level = models.PositiveIntegerField(default = 0)
    template = models.CharField(max_length = 50, null = True, blank = True)

class GenericMenuModel(CMSPlugin):
    """
    Model for generic menu. Makes use of 'show_menu' cms tag.
    """
    start_level = models.PositiveIntegerField(default = 0)
    end_level = models.PositiveIntegerField(default = 100)
    extra_inactive = models.PositiveIntegerField(default = 0)
    extra_active = models.PositiveIntegerField(default = 100)
    template = models.CharField(max_length = 50, null = True, blank = True)
