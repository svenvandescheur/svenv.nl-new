from rest_framework import routers

from views.api.views import ArticleViewSet


router = routers.SimpleRouter()
router.register(r'articles', ArticleViewSet)
