from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.core.signals import request_finished
from django.dispatch import Signal,receiver
from django.db.models.signals import pre_save, pre_delete, pre_init, post_init, post_save, post_delete

####### built-in signals...................

# @receiver(user_logged_in, sender=User, )
# def login_success(sender, request, user, **kwargs):
#     print("_______________________")
#     print("login successs")
#     print("sender:", sender)
#     print("request:", request)
#     print("user:", user)
#     print("user_pwd:", user.password)
#     print(f"kwargs: {kwargs}")
#
#
# @receiver(user_logged_out, sender=User, )
# def logout_success(sender, request, user, **kwargs):
#     print("_______________________")
#     print("logout user successs ....")
#     print("sender:", sender)
#     print("request:", request)
#     print("user:", user)
#     print("user_pwd:", user.password)
#     print(f"kwargs: {kwargs}")
#
#
# @receiver(request_finished)
# def my(sender, **kwargs):
#     print("Request finished!")
#
#
# @receiver(user_login_failed)
# def fail(sender, credentials, request, **kwargs):
#     print("________________")
#     print("login failed")
#     print("sender:", sender)
#     print("credentials:", credentials)
#     print("request:", request)
#     print(f'kwargs: {kwargs}')
#
#
# @receiver(pre_save, sender=User)
# def at_beginning_save(sender, instance, **kwargs):
#     print("________________")
#     print("presave signal")
#     print("sender:", sender)
#     print("instace:", instance)
#     print(f'kwargs: {kwargs}')


#### custom signals...........

notification = Signal()

@receiver(notification)
def show_notification(sender,**kwargs):
    print(sender)
    print(f'{kwargs}')
    print('Notification')