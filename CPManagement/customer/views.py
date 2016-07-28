from django.http import JsonResponse
from django.shortcuts import render
from .forms import CustomerForm
from .models import Customer
from provider.models import Provider
from django.template.context_processors import csrf


def customer_view(request):
    args = {'form': CustomerForm}
    args.update(csrf(request))

    if request.POST:
        response = {}
        if 'customer' not in request.POST:
            response['status'] = 500
        else:
            customer_id = request.POST.get('customer', 0)
            response['status'] = 200
            customer = Customer.objects.get(id=customer_id)
            region_ids = list(customer.region.filter(customer=customer_id).values_list('id'))
            providers = Provider.objects.filter(region__in=region_ids).distinct()

            providers_list = []
            for provider in providers:
                data = {'id':       provider.id,
                        'provider': provider.provider,
                        }
                providers_list.append(data)
            response['providers'] = providers_list

            return JsonResponse(response)

    return render(request, 'customer.html', args)
