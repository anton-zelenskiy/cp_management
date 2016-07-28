from django.views.generic import DetailView
from .models import Provider


class ProviderGet(DetailView):
    model = Provider
    template_name = 'provider_get.html'
