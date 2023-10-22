from django.urls import path
from .views import RestaurantCreateView, MenuCreateView, MenuTodayView, VoteCreateView, ResultView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('restaurant/create/', RestaurantCreateView.as_view(), name='restaurant-create'),
    path('menu/create/', MenuCreateView.as_view(), name='menu-create'),
    path('menu/today/', MenuTodayView.as_view(), name='menu-today'),
    path('vote/create/', VoteCreateView.as_view(), name='vote-create'),
    path('result/', ResultView.as_view(), name='result'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]