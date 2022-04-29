from django.urls import path
from .views import PatientList, PatientDetail,PatientCreate

app_name = 'patient'

urlpatterns = [
    path('', PatientList.as_view(), name='list'),
    path('create/', PatientCreate.as_view(), name='create'),
    path('<int:pk>', PatientDetail.as_view(), name='detail')
]