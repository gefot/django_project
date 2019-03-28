from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from second_app.models import Device, User
from second_app.forms import UserForm


# Class Based Views
class IndexView(TemplateView):
    template_name = 'second_app/index.html'

    # context_dict = {'text': 'hello world', 'number': '1000'}

    def get_context_data(self, **kwargs):
        context_dict = super().get_context_data(**kwargs)
        context_dict['text'] = 'hello world'
        context_dict['number'] = '1000'
        return context_dict


class SecondAppDeviceListView(ListView):
    model = Device
    template_name = 'second_app/devices.html'
    context_object_name = 'devices'


# class SecondAppDeviceDetailedView(DetailView):
#     context_object_name = 'devices_detail'
#     model = Device
#     template_name = 'second_app/devices.html'


# Function Views
def index(request):
    context_dict = {'text': 'hello world', 'number': '1000'}
    return render(request, 'second_app/index.html', context_dict)


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

    return render(request, 'second_app/users.html', {'form': form})


def second_app_forms(request):
    form = {}
    return render(request, 'second_app/forms.html', {'form': form})
