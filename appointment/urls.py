from django.urls import path
from .views import AppointmentDetail, AppointmentList,AppointmentCreate

app_name="appointment"

urlpatterns = [
    path('<int:pk>/',AppointmentDetail.as_view(), name='detail'),
    path('create/',AppointmentCreate.as_view(), name='create'),
    path('', AppointmentList.as_view(), name='list')
]

