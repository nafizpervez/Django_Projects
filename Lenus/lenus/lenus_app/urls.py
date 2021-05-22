from django.conf.urls import url
from django.urls import path
from lenus_app import views

app_name = 'lenus'

urlpatterns = [
    path('',views.index, name='index'),
    path('index',views.index, name='index'),
    path('ambu/',views.ambu, name= 'ambu'),
    path('blood/',views.blood, name= 'blood'),
    path('doc/',views.doc, name= 'doc'),
    path('fire_ser/',views.fire_ser, name= 'fire_ser'),
    path('medi/',views.medi, name= 'medi'),
    path('others/',views.others, name= 'others'),
    path('physio/',views.physio, name= 'physio'),
    path('police/',views.police, name= 'police'),
    path('services/',views.services, name= 'services'),
    path('volun/',views.volun, name= 'volun'),
    path('contact/',views.contact, name= 'contact'),
]
