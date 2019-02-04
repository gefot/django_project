import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()


import random
from second_app.models import Device, User
from faker import Faker

fakegen = Faker()


def populate_devices(N):
    for i in range(N):
        hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        mac_address = 'SEP'
        for i in range(11):
            hex = random.choice(hex_digits)
            mac_address += hex
        # print(mac_address)

        extension = str(random.randint(10000, 99999))
        # print(extension)

        reg = ['Registered', 'Unregistered']
        status = random.choice(reg)
        # print(registration_status)

        timestamp = fakegen.date_time_this_month(before_now=True, after_now=False, tzinfo=None)
        # print(timestamp)

        new_device = Device.objects.get_or_create(mac_address=mac_address, extension=extension,
                                           status=status, timestamp=timestamp)[0]
        new_device.save()
        # print('\n\n')

    print(Device.objects.all())


def populate_users(N):
    for i in range(N):
        full_name = fakegen.name().split()
        first_name = full_name[0]
        print(first_name)
        last_name = full_name[1]
        print(last_name)
        email = fakegen.email()
        print(email)

        new_user = User.objects.get_or_create(first_name=first_name, last_name=last_name, email=email)[0]
        new_user.save()

    print(User.objects.all())


if __name__ == '__main__':
    populate_devices(1)
    populate_users(1)

