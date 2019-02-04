from django.shortcuts import render
from second_app.models import Device, User
from second_app.forms import UserForm


# Create your views here.
def index(request):
    return render(request, 'second_app/index.html')


def second_app_devices(request):
    devices = Device.objects.order_by('timestamp')
    # devices = [['a1', 'a2', 'a3', 'a4', 'a5'], ['b1', 'b2', 'b3', 'b4', 'b5'], ['c1', 'c2', 'c3', 'c4', 'c5'],
    #            ['d1', 'd2', 'd3', 'd4', 'd5'], ['e1', 'e2', 'e3', 'e4', 'e5']]

    my_dict = {'devices': devices}
    return render(request, 'second_app/devices.html', context=my_dict)


def second_app_users(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error: Form Invalid')

    return render(request, 'second_app/users.html', {'form':form})


def second_app_forms(request):
    pass
    return render(request, 'second_app/forms.html', {'form': form})


