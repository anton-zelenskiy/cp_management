from django.conf.urls import url
from .views import customer_view
from dal import autocomplete
from .models import Customer


urlpatterns = [
    url(r'^$', customer_view, name='customer'),
]
