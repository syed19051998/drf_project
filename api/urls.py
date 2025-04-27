from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('employees', views.EmployeeViewset, basename='employees') #basename is only required when viewset.viewset is used in Views.py


urlpatterns = [
    # # For Student App
    # path('students/', views.studentsViews),
    # path('students/<int:pk>/', views.studentDetailView),

    #For Employee App
    # path('employees/', views.Employees.as_view()),
    # path('employees/<int:pk>/', views.EmployeeDetail.as_view()),

    path('', include(router.urls)),

    path('blogs/', views.BlogsView.as_view()),
    path('comments/', views.CommentsView.as_view()),
    path('blogs/<int:pk>/', views.BlogDetailView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view()),
]