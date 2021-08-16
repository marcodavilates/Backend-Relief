from django.shortcuts import render
from .models import videoLink
from .serializers import videoSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#creating an Modal View to list all the video History + Add videos to the History

class VideoHistory(APIView):

#Search and specific video on the database
    def search(self, url):
        video = videoLink.objects.get(urlVideo=url)
        return(videoSerializer(video))


#If we got a GET request, the server'll send a list of all the history 

    def get(self, request):
        videos = videoLink.objects.all()
        serializer = videoSerializer(videos, many=True)
        return Response(serializer.data)


#If we got a POST request, the server'll create a new video on the history, only if this video is a new URL. We add a PK in the model of the videoLink

    def post(self, request):
        serializer = videoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        videosearch = self.search(request.data['urlVideo'])
        return Response(videosearch.data, status=status.HTTP_200_OK)




#This function return a list of all the videos that has marked like bookmark, when the bolean field bookmark == True
class VideoBookmarks(APIView):

    def get(self, request):
        videos = videoLink.objects.all().filter(bookmark=True)
        serializer = videoSerializer(videos, many=True)
        return Response(serializer.data)
    

#This function update the value of the bookmarks

    def put(self, request):
            bookmarkVideo = videoLink.objects.get(urlVideo=request.data["urlVideo"])
            serializer = videoSerializer(bookmarkVideo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(status=status.HTTP_400_BAD_REQUEST)