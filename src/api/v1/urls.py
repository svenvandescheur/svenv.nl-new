from django.conf.urls import include, url

from .routers import router


urlpatterns = [
    url(r'', include(router.urls), name='router'),
]
