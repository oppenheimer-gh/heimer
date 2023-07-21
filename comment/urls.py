from django.urls import path

from comment import views

urlpatterns = [
    path('post/<uuid:post_id>/', views.GetCreateCommentAPIView.as_view(), name='comment-post'),
    path('delete/<uuid:comment_id>/', views.DeleteCommentAPIView.as_view(), name='delete'),
]
