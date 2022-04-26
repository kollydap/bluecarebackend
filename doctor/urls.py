from django.urls import path
from .views import DoctorList, DoctorDetail

app_name = 'doctor'

urlpatterns = [
    path('', DoctorList.as_view(), name='list'),
    path('<int:pk>', DoctorDetail.as_view(), name='detail')
]
