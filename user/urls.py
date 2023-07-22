from django.urls import path

from user import views

urlpatterns = [
    path('register/', views.RegisterAPIView.as_view(), name='register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('logout/', views.LogoutAPIView.as_view(), name='logout'),
    path('get/', views.GetUserView.as_view(), name='get'),
    path('mentor/get/', views.GetMentorView.as_view(), name='get-mentor'),
    path('mentor/toggle/', views.ToggleMentorView.as_view(), name='toggle-mentor'),
    path('mentee/get/', views.GetMenteeView.as_view(), name='get-mentee'),
    path('mentee/update-mentor', views.UpdateMenteeMentorView.as_view(), name='update-mentee-mentor'),
]
