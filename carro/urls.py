from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import CarroViews

router = DefaultRouter(trailing_slash=False)
router.register(r'carro/', CarroViews)

urlpatterns = [
    url(r'', include(router.urls))
]