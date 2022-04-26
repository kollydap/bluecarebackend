from django.urls import path
from .views import PatientList, PatientDetail

app_name = 'patient'

urlpatterns = [
    path('', PatientList.as_view(), name='list'),
    path('<int:pk>', PatientDetail.as_view(), name='detail')
]
