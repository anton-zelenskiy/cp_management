from django.conf.urls import url
from .views import ProviderGet

urlpatterns = [
    url(r'^get/(?P<pk>\d+)/$', ProviderGet.as_view(), name='provider_get'),
]
