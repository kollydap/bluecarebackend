from django.urls import path
from .views import UserCreate
# , BlacklistTokenView

app_name = 'account'

urlpatterns = [
    path('register/', UserCreate.as_view(), name="create_user"),
    # path('logout/', BlacklistTokenView.as_view(), name='blacklist')
]
    