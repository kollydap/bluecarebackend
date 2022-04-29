from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/doctor/', include('doctor.urls', namespace='doctor')),
    path('api/patient/', include('patient.urls', namespace='patient')),
    path('api/account/', include('account.urls', namespace='users')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/appointment/', include('appointment.urls', namespace='appointment')),
    path('api/token/' ,TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

