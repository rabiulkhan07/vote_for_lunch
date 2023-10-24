from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls.static import static
from django.conf import settings

from .views import RestaurantCreateView,RestaurantListView,RestaurantDetailView,RestaurantEditView,RestaurantDeleteView,MenuCreateView,MenuListView,MenuDetailView,MenuUpdateView,TodayMenuView,VoteCreateView,CalculateResultView
from . import views

urlpatterns = [
    path('restaurant/create/', RestaurantCreateView.as_view(), name='restaurant-create'),
    path('restaurants/', RestaurantListView.as_view(), name='restaurant-list'),
    path('restaurants/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant-detail'),
    path('restaurants/<int:pk>/edit/', RestaurantEditView.as_view(), name='restaurant-edit'),
    path('restaurants/<int:pk>/delete/', RestaurantDeleteView.as_view(), name='restaurant-delete'),
    path('menu/create/', MenuCreateView.as_view(), name='menu-create'), 
    path('menus/', MenuListView.as_view(), name='menu-list'),
    path('menus/<int:pk>/', MenuDetailView.as_view(), name='menu-detail'),
    path('menus/<int:pk>/edit/', MenuUpdateView.as_view(), name='menu-edit'),
    path('menus/<int:pk>/delete/', MenuUpdateView.as_view(), name='menu-delete'),
    path('menus/today/', TodayMenuView.as_view(), name='today-menu'),
    path('votes/create/', VoteCreateView.as_view(), name='vote-create'),
    path('get_result/', CalculateResultView.as_view(), name='get_result'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


