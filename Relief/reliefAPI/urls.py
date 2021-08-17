from django.urls import path
from .views import VideoHistory, VideoBookmarks



urlpatterns = [
    path('', VideoHistory.as_view()),
    path('bookmarks',VideoBookmarks.as_view()),
]
