from cms.models.pagemodel import Page
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response

from .serializers import ArticleSerializer


class CardPagination(PageNumberPagination):
    """
    Pagination class for card view.
    Uses 12 items per page (can be divided by 1, 2, 3, 4 and 6).
    """
    page_size = 12


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A paginated API endpoint for browsing articles.
    """
    model = Page
    pagination_class = CardPagination
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer, TemplateHTMLRenderer]
    serializer_class = ArticleSerializer
    template_name = 'children.html'

    queryset = Page.objects.get_home()\
        .get_descendants()\
        .filter(template='{}.html'.format(
            Page.objects.get_home().categoryextension.children_template_name)
        )\
        .reverse()

    def list(self, request, *args, **kwargs):
        """
        I have no idea why this works.
        http://stackoverflow.com/questions/18925358/how-do-you-access-data-in-the-template-when-using-drf-modelviewset-and-templateh
        """
        response = super(ArticleViewSet, self).list(request, *args, **kwargs)
        if request.accepted_renderer.format == 'html':
            return Response({'children': response.data['results']}, template_name=self.template_name)
        return response
