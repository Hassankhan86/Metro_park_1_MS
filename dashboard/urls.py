from django.contrib import admin
from django.urls import path

from .import views
app_name = "dashboard"

urlpatterns = [
    path('', views.homepage, name='homepage'),

    path('form/', views.booking, name='booking'),
    path('details/', views.details, name='details'),
    # path('bk_form/', views.bk_form, name='bk_form'),

    path('contact_us/', views.contact_us, name='contact_us'),
    path('services/', views.services, name='services'),
    path('career/', views.career, name='career'),

    path('update_info/<id>/', views.update_info, name='update_info'),
    path('bookingm2m/<str:pk_test>', views.bookingm2m, name='bookingm2m'),   #not Working Remove it
    path('alterbooking/', views.alterbooking, name='alterbooking'),
    path('savealterbooking/', views.savealterbooking, name='savealterbooking'),
    path('confirmbooking/', views.confirmbooking, name='confirmbooking'),

]
