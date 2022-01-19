from .serializers import(
    User_Register,
    
)
from usermanager.models import User
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated , AllowAny

class User_APIView (generics.ListCreateAPIView):
    # queryset will get evaluated once, and those results will be cached for all subsequent requests.
    queryset = User.objects.all()
    serializer_class = User_Register
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = User_Register(data=request.data)
        if serializer.is_valid():
            user = self.perform_create(serializer)
            print('\ncreated\n')
            token = Token.objects.create(user=user)
            return Response(
                {
                    "user": {
                        "groups": serializer.data["groups"],
                        "username": serializer.data["username"],
                        "id" : serializer.data["id"]
                    },
                    "status": {
                        "message": "User created",
                        "code": f"{status.HTTP_200_OK} OK",
                    },
                    "token": token.key,
                }
            )
        return Response(
            {
                "error": serializer.errors,
                "status": f"{status.HTTP_203_NON_AUTHORITATIVE_INFORMATION} \ NON AUTHORITATIVE INFORMATION",
            }
        )

    def perform_create(self, serializer):
        user = serializer.save()
        # user is the username actually
        return user
 
 
