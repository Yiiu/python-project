from django.conf.urls import url, include
from django.contrib import admin

from . import view
# url配置，就相当于routes
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('app.urls')),
]
