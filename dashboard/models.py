from django.contrib.auth.models import User
from django.db import models

# class Temp(models.Model):
#     search_name = models.TextField(blank=True, max_length="10000")
#     from_date_tem = models.TextField(blank=True, max_length="10000")
#
#
#     def __str__(self):
#         return f"{self.search_name} + {self.from_date_tem} "

# Create your models here.
class customer(models.Model):

    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    customer_name = models.TextField(blank=True, max_length="200")
    customer_id = models.TextField(blank=True, max_length="50")
    customer_phone = models.TextField(blank=True,max_length="50")
    customer_email = models.TextField(blank=True,max_length="50")
    vehicle_number = models.TextField(blank=True, max_length="50")
    vehicle_name = models.TextField(blank=True,max_length="50")
    vehicle_color = models.TextField(blank=True,max_length="50")
    # vehicle_documents = models.FileField(blank=False, null=False, default='default.png')

    vehicle_documents =  models.FileField(upload_to='documents/%Y/%m/%d')


    def __str__(self):
        return f"{self.customer_name}+{self.vehicle_number}+{self.vehicle_name}  "


class Key_table(models.Model):
    key_name = models.TextField(blank=True, max_length='100')

    def __str__(self):
        return f"{self.key_name}"

class Slot_duration_table(models.Model):
    from_date = models.TextField(blank=True, max_length='100')
    to_date = models.TextField(blank=True, max_length='100')

    def __str__(self):
        return f"{self.from_date} + {self.to_date}"

class parking_spaces(models.Model):
    spcae_pic = models.ImageField(blank=False, null=False, default='default.png')
    space_name = models.TextField(blank=True, max_length="100")
    space_address = models.TextField(blank=True, max_length="1000")
    total_slots = models.IntegerField(blank=True)
    key_words = models.ManyToManyField(Key_table, blank=True)
    # slot_booking = models.ManyToManyField(slots_booking_table, blank=True)
    # slot_monthly_rates = models.IntegerField(blank=True)
    slot_rates = models.IntegerField(blank=True)

    def __str__(self):
        return f"{self.space_name}"

class slots_booking_table(models.Model):
    # slot_name = models.TextField(blank=True, max_length='100')
    Slot_duration = models.ForeignKey(Slot_duration_table, blank=True,on_delete=models.CASCADE)
    customer_info = models.ForeignKey(customer, blank=True,on_delete = models.CASCADE)
    parking_name = models.ForeignKey(parking_spaces,null=True, blank=True,on_delete = models.CASCADE)

    total_price =  models.TextField(blank=True, max_length='100')


    def __str__(self):
        return f" {self.Slot_duration} + {self.customer_info}"


