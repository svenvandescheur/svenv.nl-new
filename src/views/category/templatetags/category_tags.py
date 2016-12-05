from django import template
from django.core.paginator import Paginator

register = template.Library()

@register.inclusion_tag('children.html', takes_context=True)
def children(context, root):
    """
    Renders all children of root where template matches children_template_name.
    """
    queryset = root.get_descendants().filter(template='{}.html'.format(root.categoryextension.children_template_name))
    children_per_page = 12
    page = context.request.GET.get('page', 1)
    p = Paginator(queryset, children_per_page)
    children = p.page(page)

    for child in children:
        child.computed_body = ''

        for placeholder in child.get_placeholders():
            for plugin in placeholder.get_plugins():
                child.computed_body += plugin.render_plugin(context)



    return {
        'children': children,
    }
