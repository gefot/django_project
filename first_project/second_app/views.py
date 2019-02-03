from django.shortcuts import render
from second_app.models import DN, Device
from second_app import forms

# Create your views here.
def second_app_main(request):
    dns = DN.objects.order_by('extension')
    devices = Device.objects.order_by('timestamp')
    # devices = [['a1', 'a2', 'a3', 'a4', 'a5'], ['b1', 'b2', 'b3', 'b4', 'b5'], ['c1', 'c2', 'c3', 'c4', 'c5'],
    #            ['d1', 'd2', 'd3', 'd4', 'd5'], ['e1', 'e2', 'e3', 'e4', 'e5']]

    my_dict = {'extensions': dns, 'devices': devices}
    return render(request, 'second_app/phones.html', context=my_dict)


def second_app_main_forms(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # Do something
            print("VALIDATION IS SUCCESS")
            print("NAME: "+form.cleaned_data['mac_address'])
            print("DESCRIPTION: " +form.cleaned_data['description'])
            print("STATUS: " +form.cleaned_data['registration_status'])
            print("TEXT: " +form.cleaned_data['text'])


    return render(request, 'second_app/forms.html', {'form': form})




