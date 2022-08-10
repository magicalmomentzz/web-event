from django.urls import path
from . import views

urlpatterns = [

    path('', views.index , name="eventregisterhome"),
    path('help', views.help , name="eventregisterhelp"),
    path('checkout', views.checkout , name="eventregistercheckout"),
    path('handlerequest/', views.handlerequest , name="handlerequest"),
    


]