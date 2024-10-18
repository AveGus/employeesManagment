from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.response import Response

from .models import Employee, Position
from .serializers import EmployeeSerializer, UserRegistrationSerializer, PositionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class EmployeeListView(generics.ListAPIView):
    serializer_class = EmployeeSerializer

    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Employee.objects.all()
        is_fired = self.request.query_params.get('is_fired', None)
        filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
        filterset_fields = ['is_fired']
        if is_fired is not None:
            queryset = queryset.filter(is_fired=is_fired)
        return queryset


def user_list_view(request):
    employees = Employee.objects.all()  # Получаем всех сотрудников из базы данных
    return render(request, 'index.html', {'employees': employees})  # Рендерим шаблон


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User created successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH']:
            return [permissions.IsAuthenticated()]
        elif self.request.method == 'DELETE':
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]



class PositionListCreateView(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [permissions.IsAdminUser]