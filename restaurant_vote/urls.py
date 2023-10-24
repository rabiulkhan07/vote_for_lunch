from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls.static import static
from django.conf import settings

from .views import RestaurantCreateView,RestaurantListView,RestaurantDetailView,RestaurantEditView,RestaurantDeleteView


urlpatterns = [
    path('restaurant/create/', RestaurantCreateView.as_view(), name='restaurant-create'),
    path('restaurants/', RestaurantListView.as_view(), name='restaurant-list'),
    path('restaurants/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant-detail'),
    path('restaurants/<int:pk>/edit/', RestaurantEditView.as_view(), name='restaurant-edit'),
    path('restaurants/<int:pk>/delete/', RestaurantDeleteView.as_view(), name='restaurant-delete')


    
]


