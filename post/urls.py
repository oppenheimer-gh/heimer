from django.urls import path

from post import views

urlpatterns = [
    path('add/', views.CreatePostAPIView.as_view(), name='add'),
]
