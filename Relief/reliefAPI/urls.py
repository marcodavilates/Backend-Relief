from django.urls import path, include
from .views import VideoHistory, VideoBookmarks


urlpatterns = [
    path('', VideoHistory.as_view()),
    path('bookmarks',VideoBookmarks.as_view()),
]
