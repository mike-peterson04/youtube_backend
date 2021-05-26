
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('<video_id>/', views.VideoComment.as_view()),
    path('<video_id>/<int:comment_id>', views.CommentActions.as_view()),
    path('<video_id>/<int:comment_id>/<action>', views.CommentReview.as_view())
]
