from django.urls import path

from user import views

urlpatterns = [
    path('register/', views.RegisterAPIView.as_view(), name='register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('get/', views.GetUserView.as_view(), name='get'),
]
