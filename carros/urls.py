from django.contrib import admin
from django.urls import include
from django.conf.urls import url

urlpatterns = [
    url(r'^', include('carro.urls')),
    url(r'^admin/', admin.site.urls),
]
