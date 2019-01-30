from django.shortcuts import render
from second_app.models import DN, Device


# Create your views here.
def second_app_main(request):
    dns = DN.objects.order_by('extension')
    devices = Device.objects.order_by('timestamp')

    my_dict = {'extensions': dns, 'devices': devices}
    return render(request, 'second_app/phones.html', context=my_dict)
