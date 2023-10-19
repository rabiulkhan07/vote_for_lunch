from django.urls import path
from .views import RegisterView,GetAllUserView,GetSingleData,LoginView,EmployeeView,LogoutView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('employee', GetAllUserView.as_view()),
    path('employee/<int:user_id>', GetSingleData.as_view(), name='delete_user'),
    path('login', LoginView.as_view()),
    path('activeuser', EmployeeView.as_view()),
    path('logout', LogoutView.as_view())
]