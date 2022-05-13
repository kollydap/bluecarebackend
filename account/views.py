from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterUserSerializer,AccountSerializer 
from rest_framework.permissions import  AllowAny,IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


class UserCreate(APIView):
    permission_classes= [AllowAny]
    authentication_classes = []
    
    def post(self, request):
        reg_serializer= RegisterUserSerializer(data=request.data)
        if reg_serializer.is_valid():
            newuser = reg_serializer.save()
            if newuser:
                return Response(status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetUser(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        serializer = AccountSerializer(user)
        return(Response(data=serializer.data))
    
    
class BlacklistTokenView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        try:
            # we request for the users refresh token
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            # then we blacklist it
            token.blacklist()
        except Exception as e:
            return Response(status = status.HTTP_400_BAD_REQUEST)