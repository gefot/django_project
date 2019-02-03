import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()


import random
from second_app.models import DN, Device
from faker import Faker

fakegen = Faker()

for i in range(1):
    extension = str(random.randint(10000, 99999))
    # print(extension)
    callername = fakegen.name()
    # print(callername)

    dn = DN.objects.get_or_create(extension=extension, callername=callername)[0]
    dn.save()
    # print('\n\n')

    hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    mac_address = 'SEP'
    for i in range(11):
        hex = random.choice(hex_digits)
        mac_address += hex
    # print(mac_address)

    rand = str(random.randint(10, 100))
    description = "IT - {}".format(rand)
    # print(description)

    reg = ['Registered', 'Unregistered']
    registration_status = random.choice(reg)
    # print(registration_status)

    timestamp = fakegen.date_time_this_month(before_now=True, after_now=False, tzinfo=None)
    # print(timestamp)

    mac = Device.objects.get_or_create(mac_address=mac_address, description=description, dn=dn,
                                       registration_status=registration_status, timestamp=timestamp)[0]
    mac.save()
    # print('\n\n')

# print(DN.objects.all())
