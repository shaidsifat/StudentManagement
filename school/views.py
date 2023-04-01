from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Classes,Subject,Student
from school.serializers import ClassSerializer
from django.db.models import Q

#GET AND POST API FOR CLASS
class ListofclassApiView(APIView):
    """Delivery task status get Api view."""
    #permission_classes = [IsAdminUser]
   
    
    

    def get(self, request, format=None):
        
        
            
            snippets = Classes.objects.all()
            serializer = ClassSerializer(snippets, many=True)
            return Response(serializer.data)
      
    
    def post(self, request, format=None):
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        
    
    
# Class delete modify api view    
class ListofclassApideleteView(APIView):
    
    
    def delete(self, request, pk, format=None):
        
        if request.user.is_teacher:
            snippet = Classes.objects.get(name=pk)
            snippet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"message":"user is not teacher"})
    
    def put(self, request, pk, format=None):
        
        if request.user.is_teacher:
            snippet = Classes.objects.get(name=pk)
            serializer = ClassSerializer(snippet, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message":"user is not teacher"})
    
# Filter APi for class and subject  
class FilterApiview(APIView):
    
    permission_classes = [IsAdminUser]
    
    def get(self, request):
        
        #class = request.query_params.get('class')
        subject = request.query_params.get('subject')
        Classes = request.query_params.get('class')
        if subject:
            query = Classes.objects.filter( Q(name=Classes) | Q(last_name__startswith='D')).values('gpa')
            return Response({"message": query})
        else:
            query = Classes.objects.filter(name=Classes).values('gpa')
            return Response({"message": query})