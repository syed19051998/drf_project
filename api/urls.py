from django.urls import path
from . import views

urlpatterns = [
    # For Student App
    path('students/', views.studentsViews),
    path('students/<int:pk>/', views.studentDetailView),

    # For Employee App
    path('employees/', views.Employees.as_view()),
    path('employees/<int:pk>/', views.EmployeeDetail.as_view())
]