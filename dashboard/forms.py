from django import forms
from . import models






class Customer_details(forms.ModelForm):
    class Meta:
        model = models.customer
        fields = ['customer_name', 'customer_id', 'customer_phone', 'customer_email', 'vehicle_number', 'vehicle_name',
                  'vehicle_color','vehicle_documents']



    def __init__(self, *args, **kwargs):
        super(Customer_details, self).__init__(*args, **kwargs)
        self.fields['customer_name'].widget.attrs['placeholder'] = 'Full Name'
        self.fields['customer_id'].widget.attrs['placeholder'] = 'Identity Number'
        self.fields['customer_phone'].widget.attrs['placeholder'] = 'Phone Number'
        self.fields['customer_email'].widget.attrs['placeholder'] = 'Email Address @gmail.com'
        self.fields['vehicle_number'].widget.attrs['placeholder'] = 'GF 20 WSN'
        self.fields['vehicle_name'].widget.attrs['placeholder'] = 'e.g. Ford 2005'
        self.fields['vehicle_color'].widget.attrs['placeholder'] = 'White,Blue,Black .....'

        # self.fields['customer_name'].widget.attrs['required'] = 'required'
        # self.fields['customer_id'].widget.attrs['required'] = 'required'
        # self.fields['customer_phone'].widget.attrs['required'] = 'required'
        # self.fields['customer_email'].widget.attrs['required'] = 'required'
        # self.fields['vehicle_number'].widget.attrs['required'] = 'required'
        # self.fields['vehicle_name'].widget.attrs['required'] = 'required'
        # self.fields['vehicle_color'].widget.attrs['required'] = 'required'

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = ' form-control'
            visible.field.widget.attrs['style'] = 'height: 34px; width: 555px; resize:none'
            visible.field.widget.attrs['resize'] = 'none'
            # visible.field.widget.attrs['max'] = '1'
            # visible.field.widget.attrs['min'] = '0'


class slots_booking(forms.ModelForm):
    class Meta:
        model = models.slots_booking_table
        fields = ['Slot_duration','customer_info','total_price','parking_name']


    def __init__(self, *args, **kwargs):
        super(slots_booking, self).__init__(*args, **kwargs)
        # self.fields['slot_name'].widget.attrs['placeholder'] = 'slot_name'
        self.fields['Slot_duration'].widget.attrs['placeholder'] = 'Slot_duration'


        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = ' form-control,'
            visible.field.widget.attrs['style'] = 'height: 34px; width: 555px; resize:none'
            visible.field.widget.attrs['resize'] = 'none'

            # visible.field.widget.attrs['max'] = '1'
            # visible.field.widget.attrs['min'] = '0'

class parking_spaces_form(forms.ModelForm):
    class Meta:
        model = models.parking_spaces
        fields = ['spcae_pic','space_name','space_address','total_slots','key_words','slot_rates']


# class slot_duration_table_form(forms.ModelForm):
#     class Meta:
#         model = models.Slot_duration_table
#         fields = ['Slot_duration_table']