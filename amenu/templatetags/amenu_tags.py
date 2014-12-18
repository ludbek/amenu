from classytags.arguments import IntegerArgument, Argument, StringArgument
from classytags.core import Options
from classytags.helpers import InclusionTag
from django import template

register = template.Library()

class RenderMenu(InclusionTag):
    """
    Renders children of given menu to given depth.
    """
    name = "render_menu"
    template = "amenu/render_menu.html"

    options = Options(
        Argument('page', required=True),
        IntegerArgument('depth', required=True),
    )

    def get_context(self, context, page, depth):
        if depth is not 0:
            context['depth'] = depth - 1
            context['pages'] = page.get_children()
        else:
            context = None
        return context


register.tag(RenderMenu)
