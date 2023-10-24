
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from rest_framework.exceptions import AuthenticationFailed
from .models import Restaurant,Menu
from .serializers import RestaurantSerializer,MenuSerializer
import jwt
from .permissions import IsAuthenticatedWithJWT
from django.utils import timezone

class RestaurantCreateView(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def perform_create(self, serializer):
        # Get the user from the JWT token stored in the cookie
        jwt_token = self.request.COOKIES.get('jwt')
        
        if jwt_token:
            try:
                payload = jwt.decode(jwt_token, 'secret', algorithms=['HS256'])
                user_id = payload.get('id')
                
                # Set the user as the creator of the restaurant
                serializer.save(created_by_id=user_id)
            except jwt.ExpiredSignatureError:
                raise AuthenticationFailed('Unauthenticated')
        else:
            raise AuthenticationFailed('Unauthenticated')

#Fetch Resturents
class RestaurantListView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticatedWithJWT]

#fetch single 
class RestaurantDetailView(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticatedWithJWT]

#Update
class RestaurantEditView(generics.UpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticatedWithJWT]

#delete
class RestaurantDeleteView(generics.DestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

#Menu create
class MenuCreateView(generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticatedWithJWT]

#Fetch All
class MenuListView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticatedWithJWT]
#fetch single 
class MenuDetailView(generics.RetrieveAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticatedWithJWT]

#Update
class MenuUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticatedWithJWT]

#Today Menu
class TodayMenuView(ListAPIView):
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticatedWithJWT]
    def get_queryset(self):
        today = timezone.now().date()  # Get today's date
        return Menu.objects.filter(date=today)