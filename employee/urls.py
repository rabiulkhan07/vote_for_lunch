from django.urls import path
from .views import RegisterView,GetAllUserView,GetSingleData,LoginView,EmployeeView,LogoutView

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('employee', GetAllUserView.as_view(), name='employee'),
    path('employee/<uuid:user_id>', GetSingleData.as_view(), name='single_user'),
    path('login', LoginView.as_view(), name='login'),
    path('activeuser', EmployeeView.as_view(), name='activeuser'),
    path('logout', LogoutView.as_view(), name='logout')
]