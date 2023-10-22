from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import Restaurant, Menu, Vote
from .serializers import RestaurantSerializer, MenuSerializer, VoteSerializer

class RestaurantCreateView(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class MenuCreateView(generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuTodayView(generics.RetrieveAPIView):
    serializer_class = MenuSerializer

    def get_object(self):
        today = timezone.now().date()
        menu = Menu.objects.filter(day=today).first()
        if menu:
            return menu
        return None

class VoteCreateView(generics.CreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

    def create(self, request, *args, **kwargs):
        request.data['voted_by'] = request.user.id  # Assign the currently authenticated user to voted_by
        return super().create(request, *args, **kwargs)

class ResultView(generics.ListAPIView):
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        today = timezone.now().date()
        yesterday = today - timezone.timedelta(days=1)
        three_days_ago = today - timezone.timedelta(days=3)
        
        # Check if a restaurant has won in the past three working days
        winning_restaurants = Menu.objects.filter(day__range=[three_days_ago, yesterday]).values('restaurant')
        
        queryset = Restaurant.objects.exclude(id__in=winning_restaurants)
        return queryset