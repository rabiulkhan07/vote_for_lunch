
from rest_framework import generics
from rest_framework.exceptions import AuthenticationFailed
from .models import Restaurant
from .serializers import RestaurantSerializer
import jwt
from .permissions import IsAuthenticatedWithJWT

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