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
