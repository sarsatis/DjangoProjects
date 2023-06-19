from . import views
from django.urls import path

urlpatterns = [
    path('<int:pk>/', views.employee_detail),
]