
from rest_framework import generics
from rest_framework.views import APIView 
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from rest_framework.exceptions import AuthenticationFailed
from .models import Restaurant,Menu,Vote,Result
from .serializers import RestaurantSerializer,MenuSerializer,VoteSerializer
import jwt
from .permissions import IsAuthenticatedWithJWT
from django.utils import timezone
from datetime import date, timedelta
from django.http import JsonResponse
from django.db.models import Count

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
    
#Vote
class VoteCreateView(generics.CreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticatedWithJWT]

#result
class CalculateResultView(APIView):
    def calculate_result(self):
        today = date.today()

        # Check the previous working days (e.g., last three days)
        previous_working_days = [today - timedelta(days=i) for i in range(1, 4)]

        # Get the restaurants that won on previous working days
        previous_winners = Result.objects.filter(date__in=previous_working_days).values('winner')
        previous_winner_ids = [winner['winner'] for winner in previous_winners]

        # Calculate the result for today
        today_votes = Vote.objects.filter(date=today)
        today_vote_counts = today_votes.values('restaurant').annotate(count=Count('choice'))

        # Sort the restaurants by vote count in descending order
        today_vote_counts = sorted(today_vote_counts, key=lambda x: -x['count'])

        # Find the winning restaurant for today
        winner_id = None
        for vote_count in today_vote_counts:
            if vote_count['restaurant'] not in previous_winner_ids:
                winner_id = vote_count['restaurant']
                break

        if winner_id is not None:
            # Save the result for today
            Result.objects.create(date=today, winner_id=winner_id)
            return winner_id
        else:
            return None

    def get(self, request):
        # Calculate and get the winner for today
        winner_id = self.calculate_result()

        if winner_id is not None:
            return JsonResponse({'result': f'Restaurant with ID {winner_id} is today\'s winner'})
        else:
            return JsonResponse({'result': 'No winner today'})