from django.urls import path
from .views import EmployeeListView, UserRegistrationView, user_list_view, EmployeeDetailView

urlpatterns = [
    path('employees/', EmployeeListView.as_view(), name='employee-list'),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('users/', user_list_view, name='user-list'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),

]
