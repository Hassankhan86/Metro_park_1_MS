from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.decorators import login_required
from dashboard.views import *
from dashboard.forms import *

def logoutUser(request):
    logout(request)
    return  redirect('accounts:login')


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('dashboard:homepage')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')


            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('dashboard:homepage')
            else:
                messages.info(request,"Username Or Password is Incorrect ")


    # return HttpResponse("ddasdasd")
    return render(request, 'accounts/login.html',)

def registerpage(request):
    if request.user.is_authenticated:
        return redirect('dashboard:homepage')
    else:
        form = CreateUserForm()
        print('<-------------------------------------->')
        if 'cust_name_ar' not in request.session:
            cust_name_ar = ""
            print('cust_name_ar :', cust_name_ar)
        else:
            cust_name_ar = request.session['cust_name_ar']

        if 'cust_id_no_ar' not in request.session:
            cust_id_no_ar = ""
            print('cust_id_no_ar :', cust_id_no_ar)
        else:
            cust_id_no_ar = request.session['cust_id_no_ar']

        if 'cust_phone_ar' not in request.session:
            cust_phone_ar = ""
            print('cust_phone_ar :', cust_phone_ar)
        else:
            cust_phone_ar = request.session['cust_phone_ar']

        if 'cust_mail_ar' not in request.session:
            cust_mail_ar = ""
            print('cust_mail_ar :', cust_mail_ar)
        else:
            cust_mail_ar = request.session['cust_mail_ar']

        if 'vehicle_name_ar' not in request.session:
            vehicle_name_ar = ""
            print('vehicle_name_ar :', vehicle_name_ar)
        else:
            vehicle_name_ar = request.session['vehicle_name_ar']

        if 'vehicle_number_plate_ar' not in request.session:
            vehicle_number_plate_ar = ""
            print('vehicle_number_plate_ar :', vehicle_number_plate_ar)
        else:
            vehicle_number_plate_ar = request.session['vehicle_number_plate_ar']

        if 'vehicle_color_ar' not in request.session:
            vehicle_color_ar = ""
            print('vehicle_color_ar :', vehicle_color_ar)
        else:
            vehicle_color_ar = request.session['vehicle_color_ar']

        if 'vehicle_documents_ar' not in request.session:
            vehicle_documents_ar = ""
            print('vehicle_documents_ar :', cust_mail_ar)
        else:
            vehicle_documents_ar = request.session['vehicle_documents_ar']

        if 'from_date_ar' not in request.session:
            from_date_ar = "2017-01-12T14:12"
            print('from_date_ar :', from_date_ar)
        else:
            from_date_ar = request.session['from_date1']
        from_date_ar = datetime.strptime(from_date_ar, '%Y-%m-%dT%H:%M')

        if 'to_date_ar' not in request.session:
            to_date_ar = "2017-01-12T14:12"
            print('to_date_ar :', to_date_ar)
        else:
            to_date_ar = request.session['to_date1']
        to_date_ar = datetime.strptime(to_date_ar, '%Y-%m-%dT%H:%M')

        if 'Total_Hr_ar' not in request.session:
            Total_Hr_ar = ""
            print('Total_Hr_ar :', Total_Hr_ar)
        else:
            Total_Hr_ar = request.session['Total_Hr_ar']

        if 'location_address1' not in request.session:
            ok1 = ""
            print('ok1 :', ok1)
        else:
            ok1 = request.session['location_address1']
            print(ok1)
        # print(ok1)
        # ob = parking_spaces.objects.get(space_name=ok1)

        print('<-------------------------------------->')

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()

                cus = customer(customer_name=cust_name_ar, customer_id=cust_id_no_ar, customer_phone=cust_phone_ar,
                               customer_email=cust_mail_ar, vehicle_number=vehicle_number_plate_ar,
                               vehicle_name=vehicle_name_ar,
                               vehicle_color=vehicle_color_ar, vehicle_documents=vehicle_documents_ar
                               )

                cus.user = user
                cus.save()

                # ok1 = request.session['location_address1']
                # print(ok1)
                try:
                    ob = parking_spaces.objects.get(space_name=ok1)
                    dur = Slot_duration_table(to_date=from_date_ar, from_date=to_date_ar)
                    dur.save()

                    sb = slots_booking_table()
                    sb.customer_info = cus
                    sb.Slot_duration = dur
                    sb.parking_name = ob
                    sb.total_price = Total_Hr_ar
                    sb.save()
                except:
                    print("fuck uuuu")


                # a = customer(user=cust_name_ar
                #              )
                # # customer.user =user
                # a.save()

                user = form.cleaned_data.get('username')
                messages.success(request, 'Accounts was created for ' + user)

                return redirect('accounts:login')

        context = {'form': form}
        # return HttpResponse("Register")
        return render(request, 'accounts/register.html', context)