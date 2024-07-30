from rest_framework import generics, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from mon_api.models import Personne, Player, Manager
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse
from mon_projet.serializers import PersonneSerializer, PlayerSerializer, ManagerSerializer

class PersonneRegisterView(generics.CreateAPIView):
    queryset = Personne.objects.all()
    serializer_class = PersonneSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()



class PlayerRegisterView(generics.CreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()


class ManagerRegisterView(generics.CreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()

from django.contrib.auth import authenticate, login

class PersonneLoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Please provide both username and password'}, status=400)

        user = authenticate(request, username=username, password=password)

        print('Username:', username)
        print('Password:', password)
        print('User:', user)


        if user is not None:
            print('User:', user)
            login(request, user)
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({'error': 'Invalid credentials'}, status=400)


class PersonneLogoutView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    
    def post(self, request, *args, **kwargs):
        try:
            token = request.data['refresh_token']
            refresh_token = RefreshToken(token)
            refresh_token.blacklist()
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)


   

def get_personnes(request):
    personnes = Personne.objects.all()
    serializer = PersonneSerializer(personnes, many=True)
    return JsonResponse(serializer.data, safe=False)