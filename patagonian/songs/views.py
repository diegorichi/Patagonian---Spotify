from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,mixins, status, serializers
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from .serializers import ListSongSerializer,SongSerializer
from .models import Song, Artist, Url
from .filters import SongsSearchFilter

class SongViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Song.objects.all()   
    serializer_class = ListSongSerializer
    
    def list(self, request):
        artistName_param = request.query_params.get('artistName', None)
        if not artistName_param:
             raise serializers.ValidationError('artistName is required')
        if len(artistName_param)<3:
             raise serializers.ValidationError('artistName should have more than three chars') 


        queryset = self.get_queryset().filter(artists__name__icontains=artistName_param).order_by('name')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            resp = self.get_paginated_response(serializer.data)
            return Response({
                'count':resp.data.get('count'),
                'next':resp.data.get('next'),
                'previous':resp.data.get('previous'),
                'songs':serializer.data
            })

        serializer = self.get_serializer(queryset, many=True)
        result =  { 'songs': serializer.data }
        return Response(result)

    def retrieve(self, request, pk=None):
        queryset = Song.objects.all()
        songs = queryset.filter(id=pk)
        context = {
                'request': request,
        }               
        if len(songs)==0:
                response = {"message": "Song not found"}
                return Response(response, status=status.HTTP_404_NOT_FOUND)
        
        serializer = SongSerializer(songs, many=True)
        
        
        return Response(serializer.data[0])

