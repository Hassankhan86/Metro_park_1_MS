from django.contrib import admin

# Register your models here.
from dashboard.models import customer, Key_table, slots_booking_table, parking_spaces, Slot_duration_table

admin.site.register(customer)
# admin.site.register(Key_table)
admin.site.register(slots_booking_table)
admin.site.register(parking_spaces)
# admin.site.register(Temp)
admin.site.register(Slot_duration_table)



