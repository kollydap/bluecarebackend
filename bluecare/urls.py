from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/doctor/', include('doctor.urls', namespace='doctor')),
    path('api/patient/', include('patient.urls', namespace='patient')),

    path('api/account/', include('account.urls', namespace='users')),

    path('api/appointment/', include('appointment.urls', namespace='appointment')),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

