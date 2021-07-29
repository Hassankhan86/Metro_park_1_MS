from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from datetime import datetime

from . import forms

# Create your views here.
from .forms import Customer_details
from .models import parking_spaces, slots_booking_table, Slot_duration_table, customer


def contact_us(request):
    return render(request, 'dashboard/contact_us.html')


def services(request):
    return render(request, 'dashboard/services.html')


def career(request):
    return render(request, 'dashboard/career.html')


def alterbooking(request):
    cust_mer = customer.objects.get(user=request.user)
    sp = parking_spaces.objects.all()
    ss = slots_booking_table.objects.all()

    slot_dur = Slot_duration_table.objects.filter()

    # Temp1 = Temp.objects.all()

    # print(Temp1)
    # duration = request.POST.get('options-outlined')
    # print(duration)

    # Temp.search_name.clear()

    location = request.POST.get('location_address')
    request.session['location_address1'] = location
    print(location)

    # from_date = request.session['from_date1']
    # from_date2 = datetime.strptime(from_date, '%Y-%m-%dT%H:%M')

    from_date = request.POST.get('from_date')
    to_date = request.POST.get('to_date')

    request.session['from_date1'] = from_date
    request.session['to_date1'] = to_date

    from_date1 = request.POST.get('from_date')
    from_date1 = datetime.strptime(from_date1, '%Y-%m-%dT%H:%M')
    print(from_date1)

    to_date1 = request.POST.get('to_date')
    to_date1 = datetime.strptime(to_date1, '%Y-%m-%dT%H:%M')
    print(to_date1)

    diff = to_date1 - from_date1
    print("Diff : ", diff)
    sec = diff.total_seconds()
    hours = sec / 3600
    print("Hours", hours)
    # Hrro = round(hours, 2)
    # print(Hrro)
    request.session['hourspass'] = hours

    # Temp1.delete()
    # search = Temp(search_name=location)
    # search.save()

    # from_date = datetime.strptime(from_date, '%Y-%m-%dT%H:%M')
    # print(from_date)
    # #
    # to_date = request.POST.get('to_date')
    # to_date = datetime.strptime(to_date, '%Y-%m-%dT%H:%M')
    # #
    # diff = to_date - from_date
    # print("Diff : ", diff)
    # from_date2 = request.POST.get('from_date2')
    # print(from_date2)

    #
    # dur =  Slot_duration_table(from_date=from_date)
    # dur.save()

    sp = parking_spaces.objects.filter(space_name=location)

    # request.session['Total_Price'] = Total_Hr
    # Total_Hr = request.session['Total_Price']

    form = forms.Customer_details()
    form1 = forms.slots_booking()
    print("inside Else22")

    context = {'cust_mer': cust_mer, 'sp': sp, 'hours': hours, 'to_date1': to_date1, 'from_date1': from_date1}

    return render(request, 'dashboard/alterbooking.html', context)


def savealterbooking(request):
    if request.method == 'POST':
        cust_name = request.POST.get('cust_name')
        cust_id_no = request.POST.get('cust_id_no')
        cust_phone = request.POST.get('cust_phone')
        cust_mail = request.POST.get('cust_mail')

        vehicle_name = request.POST.get('vehicle_name')
        vehicle_number_plate = request.POST.get('vehicle_number_plate')
        vehicle_color = request.POST.get('vehicle_color')
        vehicle_documents = request.FILES.get('vehicle_documents')

        # customers = customer.objects.get(user=request.user)

        # cust_save = customer(customer_name=cust_name, customer_email=cust_mail, customer_id=cust_id_no, customer_phone=cust_phone,
        #                      vehicle_name=vehicle_name,vehicle_number=vehicle_number_plate,vehicle_color=vehicle_color,vehicle_documents=vehicle_documents)
        #
        # cust_save.save()
        print('----------------------')

        from_date = request.session['from_date1']
        from_date = datetime.strptime(from_date, '%Y-%m-%dT%H:%M')
        to_date = request.session['to_date1']
        to_date = datetime.strptime(to_date, '%Y-%m-%dT%H:%M')
        hours = request.session['hourspass']

        print(from_date)
        print(to_date)
        print('Total', hours)

        print('----------------------')

        dur = Slot_duration_table(to_date=to_date, from_date=from_date)
        dur.save()

        ok1 = request.session['location_address1']
        print(ok1)

        ob = parking_spaces.objects.get(space_name=ok1)
        toobb = ob.total_slots
        print('toobb', toobb)

        rt = ob.slot_rates
        Total_Hr = rt * hours
        # tsr = slots_booking_table(total_price=Total_Hr)
        # ms.total_price =
        print(Total_Hr)
        sb = slots_booking_table()
        sb.customer_info = customer.objects.get(user=request.user)
        sb.Slot_duration = dur
        sb.parking_name = ob
        sb.total_price = Total_Hr
        sb.save()

        Remeaning = toobb - 1
        print('Total Objects', Remeaning)
        ob.total_slots = Remeaning
        ob.save()

        return details(request)

    return render(request, "dashboard/alterbooking.html")


def update_info(request, id):
    live = parking_spaces.objects.all()
    cust_mer = customer.objects.get(user=request.user)

    if request.method == 'POST':
        cust_name = request.POST.get('cust_name')
        cust_id_no = request.POST.get('cust_id_no')
        cust_phone = request.POST.get('cust_phone')
        cust_mail = request.POST.get('cust_mail')

        vehicle_name = request.POST.get('vehicle_name')
        vehicle_number_plate = request.POST.get('vehicle_number_plate')
        vehicle_color = request.POST.get('vehicle_color')
        vehicle_documents = request.FILES.get('vehicle_documents')

        cust_mer.customer_name = cust_name
        cust_mer.customer_email = cust_mail
        cust_mer.customer_id = cust_id_no
        cust_mer.customer_phone = cust_phone

        cust_mer.vehicle_name = vehicle_name
        cust_mer.vehicle_number = vehicle_number_plate
        cust_mer.vehicle_color = vehicle_color
        cust_mer.vehicle_documents = vehicle_documents

        cust_mer.save()

        return details(request)
    return render(request, 'dashboard/update.html', {'cust_mer': cust_mer})


# @login_required(login_required, name='dispatch')
# @login_required(login_url='/accounts/login')
# def booking(request):
#     parking_space1 = parking_spaces.objects.get(space_name='Link Road')
#     slb = slots_booking_table.objects.all()
#
#     if request.method == 'POST':
#
#         print("method is post")
#         form = forms.Customer_details(request.POST, request.FILES)
#
#         if form.is_valid():
#             # instance = form.save(commit=False)
#             print("inside form is valid")
#             form.save()
#
#             # # parking_space.slot_booking.add(form)
#             # abc = slots_booking_table.customer_info.add(form)
#             # parking_space1.slot_booking.add(abc)
#             # # @login_required(login_url='/accounts/login')
#             # return details(request)
#             return details(request)
#             # return HttpResponse("hjk")
#
#     form = forms.Customer_details()
#     print("inside Else")
#
#     return render(request, 'dashboard/search_form.html', {'form': form})
#
#
# @login_required(login_url='/accounts/login')
# def details(request):
#     return render(request, 'dashboard/details.html')
#
#
# def bk_form(request, location, duration, from_date):
#     sp = parking_spaces.objects.filter(space_name=location)
#
#     # x = datetime.datetime(2018, 6, 1)
#     # print(x)
#     # slout_bk = slots_booking_table.objects.all()
#     print(location)
#     print(from_date)
#     if request.method == 'POST':
#         form = forms.Customer_details()
#         if form.is_valid():
#             # instance = form.save(commit=False)
#             print("inside form is valid")
#             form.save()
#
#             # parking_space.slot_booking.add(form)
#             # abc = slots_booking_table.customer_info.add(form)
#             # sp.slot_booking.add(abc)
#         # abc = slout_bk.customer_info.save(form)
#         # sp.slot_booking.add(abc)
#         # print(duration, from_date)
#
#         return render(request, 'dashboard/search_form.html', {'form': form, 'sp': sp})
#     return HttpResponse("ghjk")
#
#
# # @login_required(login_url='/accounts/login')
# def homepage(request):
#     live = parking_spaces.objects.all()
#     duration = request.POST.get('options-outlined')
#
#     print(duration)
#     location = request.POST.get('location_address')
#     date = request.POST.get('date')
#     print(location)
#
#     if request.method == 'POST':
#         return bk_form(request, location, duration, date)
#
#     #     sp = parking_spaces.objects.all()
#     #
#     #
#     #
#     #
#     #     sp = parking_spaces.objects.filter(space_name=location)
#     #
#     #
#     #     print("inside Else22")
#     #     request.method = 'GET'
#     #     return render(request, 'dashboard/search_form.html', {'form': form,'sp':sp})
#     return render(request, 'dashboard/homepage.html', {'live': live})

def booking(request):
    live = parking_spaces.objects.all()
    # parking_space1  = parking_spaces.objects.get(space_name='Link Road')

    if request.method == 'POST':
        cust_name = request.POST.get('cust_name')
        request.session['cust_name_ar'] = cust_name

        cust_id_no = request.POST.get('cust_id_no')
        request.session['cust_id_no_ar'] = cust_id_no

        cust_phone = request.POST.get('cust_phone')
        request.session['cust_phone_ar'] = cust_phone

        cust_mail = request.POST.get('cust_mail')
        request.session['cust_mail_ar'] = cust_mail

        vehicle_name = request.POST.get('vehicle_name')
        request.session['vehicle_name_ar'] = vehicle_name
        # print('vehicle_name',vehicle_name)

        vehicle_number_plate = request.POST.get('vehicle_number_plate')
        request.session['vehicle_number_plate_ar'] = vehicle_number_plate

        vehicle_color = request.POST.get('vehicle_color')
        request.session['vehicle_color_ar'] = vehicle_color

        vehicle_documents = request.FILES.get('vehicle_documents')
        request.session['vehicle_documents_ar'] = vehicle_documents

        cust_save = customer(customer_name=cust_name, customer_email=cust_mail, customer_id=cust_id_no,
                             customer_phone=cust_phone,
                             vehicle_name=vehicle_name, vehicle_number=vehicle_number_plate,
                             vehicle_color=vehicle_color, vehicle_documents=vehicle_documents)
        # cust_save.save()
        print('----------------------')

        from_date = request.session['from_date1']
        from_date2 = datetime.strptime(from_date, '%Y-%m-%dT%H:%M')
        # request.session['from_date_ar'] = from_date2
        print('from_date', from_date2)

        to_date = request.session['to_date1']
        to_date2 = datetime.strptime(to_date, '%Y-%m-%dT%H:%M')
        # request.session['to_date_ar'] = to_date2
        print('to_date', to_date2)

        # request.session['hourspass'] = hours
        hours = request.session['hourspass']
        # request.session['hours_ar'] = hours
        print('Total', hours)

        print('----------------------')
        dur = Slot_duration_table(to_date=to_date, from_date=to_date2)
        # dur.save()

        ok1 = request.session['location_address1']
        print(ok1)
        ob = parking_spaces.objects.get(space_name=ok1)
        # request.session['ob_ar'] = ob

        toobb = ob.total_slots
        print('toobb', toobb)

        Remeaning = toobb - 1
        print('Total Objects', Remeaning)
        ob.total_slots = Remeaning
        ob.save()

        rt = ob.slot_rates
        Total_Hr = rt * hours
        request.session['Total_Hr_ar'] = Total_Hr
        # tsr = slots_booking_table(total_price=Total_Hr)
        # ms.total_price =
        print(Total_Hr)

        sb = slots_booking_table()
        sb.customer_info = cust_save
        sb.Slot_duration = dur
        sb.parking_name = ob
        sb.total_price = Total_Hr
        # sb.save()

        #     print("method is post")

        form = forms.Customer_details(request.POST, request.FILES)
        form1 = forms.slots_booking(request.POST, None)
        form2 = forms.parking_spaces_form(request.POST, None)
        # if form.is_valid() and form1.is_valid():
        #     # instance = form.save(commit=False)
        #     print("inside form is valid")

        # ss = Temp.objects.get()
        # print('ss',ss )

        # form = form.save()
        # ms = form1.save(commit=False)
        # ms.customer_info = form
        # ms.Slot_duration = dur
        # ms.parking_name = ob
        #
        # toobb = ob.total_slots
        # print('toobb', toobb)
        #
        # rt = ob.slot_rates
        # Total_Hr = rt * hours
        # # tsr = slots_booking_table(total_price=Total_Hr)
        # ms.total_price = Total_Hr
        # print(Total_Hr)
        #
        # request.session['Total_Price'] = Total_Hr
        #
        # # ob .save()
        # ms.save()
        # # ob.slot_booking.add(ms)
        # # ob.save()
        # # print(ob)
        #
        # Remeaning = toobb - 1
        # print('Total Objects', Remeaning)
        # ob.total_slots = Remeaning
        # ob.save()
        #
        # return redirect('/')
        # return confirmbooking(request)
        return details(request)

    # form = forms.Customer_details()
    print("inside Else")

    return render(request, 'dashboard/search_form.html', {'live': live})


@login_required(login_url='/accounts/login')
def confirmbooking(request):
    # dddd = request.session['vehicle_name_ar']
    name = request.session['cust_name_ar']
    print('name : ',name)
    id_no = request.session['cust_id_no_ar']
    print('name : ', id_no)
    phone = request.session['cust_phone_ar']
    print('name : ', phone)
    mail = request.session['cust_mail_ar']
    print('name : ', mail)
    vehicle_name_ar = request.session['vehicle_name_ar']
    print('name : ', vehicle_name_ar)
    vehicle_number_ar = request.session['vehicle_number_plate_ar']
    print('name : ', vehicle_number_ar)
    color_ar = request.session['vehicle_color_ar']
    print('name : ', color_ar)
    documents_ar = request.session['vehicle_documents_ar']
    print('name : ', documents_ar)

    from_date_ar = request.session['from_date1']
    from_date_ar = datetime.strptime(from_date_ar, '%Y-%m-%dT%H:%M')
    to_date_ar = request.session['to_date1']
    to_date_ar = datetime.strptime(to_date_ar, '%Y-%m-%dT%H:%M')

    Total_Hr_ar = request.session['Total_Hr_ar']

    ok1 = request.session['location_address1']
    print(ok1)
    ob = parking_spaces.objects.get(space_name=ok1)
    # user = request.user
    nw_user = customer.objects.filter(user=request.user)
    # cus = customer(vehicle_name=dddd)
    # cus.user = user
    # cus.save()
    # print(user)
    nw_user.customer_name = name
    nw_user.customer_id = id_no
    nw_user.customer_phone = phone
    nw_user.customer_email = mail
    nw_user.vehicle_name = vehicle_name_ar
    nw_user.vehicle_number = vehicle_number_ar
    nw_user.vehicle_color = color_ar
    # nw_user.customer_name = request.user.username
    nw_user.save()
    # cus.user = user
    # print('vehicle_name_ar : ',dddd)

    return render(request, 'dashboard/confirmbooking.html')


@login_required(login_url='/accounts/login')
def details(request):
    live = parking_spaces.objects.all()
    # customers = customer.objects.get(user=request.user)
    # slot_booking = customers.slots_booking_table_set.all()
    # print(ss)

    slot_booking = request.user.customer.slots_booking_table_set.all()
    # Profile.objects.filter(user=request.user).first()
    customers = customer.objects.filter(user=request.user)
    cust = customer.objects.get(user=request.user)

    print("=======================================")
    print(customers)
    print("=======================================")

    # print(slot_booking)

    context = {}

    return render(request, 'dashboard/details.html',
                  {'live': live, "customers": customers, "slot_booking": slot_booking, "cust": cust})


# @login_required(login_url='/accounts/login')
def homepage(request, ):
    live = parking_spaces.objects.all()

    if request.method == 'POST':
        sp = parking_spaces.objects.all()
        ss = slots_booking_table.objects.all()

        slot_dur = Slot_duration_table.objects.filter()

        # Temp1 = Temp.objects.all()

        # print(Temp1)
        # duration = request.POST.get('options-outlined')
        # print(duration)

        # Temp.search_name.clear()

        location = request.POST.get('location_address')
        request.session['location_address1'] = location
        print(location)

        # from_date = request.session['from_date1']
        # from_date2 = datetime.strptime(from_date, '%Y-%m-%dT%H:%M')

        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')

        request.session['from_date1'] = from_date
        request.session['to_date1'] = to_date

        from_date1 = request.POST.get('from_date')
        from_date1 = datetime.strptime(from_date1, '%Y-%m-%dT%H:%M')
        print(from_date1)

        to_date1 = request.POST.get('to_date')
        to_date1 = datetime.strptime(to_date1, '%Y-%m-%dT%H:%M')
        print(to_date1)

        diff = to_date1 - from_date1
        print("Diff : ", diff)
        sec = diff.total_seconds()
        hours = sec / 3600
        print("Hours", hours)
        # Hrro = round(hours, 2)
        # print(Hrro)
        request.session['hourspass'] = hours

        # Temp1.delete()
        # search = Temp(search_name=location)
        # search.save()

        # from_date = datetime.strptime(from_date, '%Y-%m-%dT%H:%M')
        # print(from_date)
        # #
        # to_date = request.POST.get('to_date')
        # to_date = datetime.strptime(to_date, '%Y-%m-%dT%H:%M')
        # #
        # diff = to_date - from_date
        # print("Diff : ", diff)
        # from_date2 = request.POST.get('from_date2')
        # print(from_date2)

        #
        # dur =  Slot_duration_table(from_date=from_date)
        # dur.save()

        sp = parking_spaces.objects.filter(space_name=location)

        # request.session['Total_Price'] = Total_Hr
        # Total_Hr = request.session['Total_Price']

        form = forms.Customer_details()
        form1 = forms.slots_booking()
        print("inside Else22")
        # request.method = 'GET
        # return location
        return render(request, 'dashboard/search_form.html',
                      {'form1': form1, 'form': form, 'sp': sp, 'ss': ss, "from_date1": from_date1, "to_date1": to_date1,
                       "hours": hours, 'live': live})
    return render(request, 'dashboard/homepage.html', {'live': live})


def bookingm2m(request, pk_test):
    live = parking_spaces.objects.all()
    customers = customer.objects.get(id=pk_test)
    slot_booking = customers.slots_booking_table_set.all()
    form = forms.slots_booking(request.POST, None)

    context = {"customers": customers, "form": form, "slot_booking": slot_booking, 'live': live}

    return render(request, "dashboard/bookingm2m.html")
