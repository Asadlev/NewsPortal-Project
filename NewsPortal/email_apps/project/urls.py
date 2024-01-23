from django.urls import path
from .views import AppointmentView


app_name = 'appointment'

urlpatterns = [
   path('', AppointmentView.as_view(), name='project/index'),
]