from django.urls import path

from post import views

urlpatterns = [
    path('add/', views.CreatePostAPIView.as_view(), name='add'),
    path('', views.GetAllPostAPIView.as_view(), name='all'),
    path('<uuid:post_id>/', views.GetPostAPIView.as_view(), name='get'),
]
