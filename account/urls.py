from django.urls import path
from .views import UserCreate, BlacklistTokenView,GetUser

app_name = 'account'

urlpatterns = [
    path('register/', UserCreate.as_view(), name="create_user"),
    path('logout/', BlacklistTokenView.as_view(), name='blacklist'),
    path('getuser/',GetUser.as_view(), name='get_user' )
]
    