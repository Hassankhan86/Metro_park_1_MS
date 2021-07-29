# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from django.dispatch import receiver
#
# from django.contrib.auth.models import Group
# from dashboard.models import customer
# from dashboard.views import *
# from dashboard.forms import *
#
#
# @receiver(post_save, sender=User)
# def customer_profile(sender, instance, created, **kwargs):
#     if created:
#         customer.objects.create(
#             user=instance,
#             customer_name=instance.username,
#             customer_email=instance.email,
#             # customer_phone=instance.Customer_details.customer_phone,
#
#
#
#         )
#
#         # group = Group.objects.get(name='customer')
#         # instance.groups.add(group)
#         # customer.objects.create(
#         #     user=instance,
#         #     name=instance.username,
#         # )
#         # print('Profile Created')
#
# post_save.connect(customer_profile,sender=User)