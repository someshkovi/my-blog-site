from datetime import datetime
from django.contrib.auth import get_user_model
from django.db import models
from allauth.account.signals import user_logged_in, user_signed_up

User = get_user_model()


def user_logged_in_receiver(request, user, **kwargs):
    print(request)
    print(f'{user} logged in at {datetime.now()}')


def user_signed_up_receiver(request, user, **kwargs):
    print(request)
    print(f'{user} signed up at {datetime.now()}')


user_signed_up.connect(user_signed_up_receiver)

user_logged_in.connect(user_logged_in_receiver, sender=User)

