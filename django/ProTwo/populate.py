import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

from AppTwo.models import User
from faker import Faker

my_faker = Faker()
def populate(N=5):
    for entry in range(N):
        fake_name = my_faker.name().split()
        fake_fname = fake_name[0]
        fake_lname = fake_name[1]
        fake_mail = my_faker.ascii_email()
        user = User.objects.get_or_create(first_name=fake_fname,last_name=fake_lname,e_mail=fake_mail)[0]
        user.save()

if __name__ == '__main__':
    populate()
