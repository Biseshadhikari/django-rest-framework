from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import *
from .Serializers import TodolistSerializer
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt


def index(request): 
    return render(request,'index.html')


@api_view(['GET'])
def home(request): 
    todolists = Todolist.objects.all()
    serializers = TodolistSerializer(todolists,many = True)
    
    return Response(serializers.data)



@api_view(['POST'])
def createTodo(request): 
    
    if request.method == "POST":
        
        serializers = TodolistSerializer(data = request.data)

        if serializers.is_valid():
            print(request.data['title'])
            checktodo = Todolist.objects.filter(title = request.data['title']).first()
            if checktodo: 
                return Response({'error':"data already exist"})
            serializers.save()
            return Response({'success':'data saved successfully'})
        return Response({'error':"data not saved"})
    
@api_view(['DELETE'])
def deleteTodo(request, id):
    try:
        todo = Todolist.objects.get(id=id)
        todo.delete()
        return JsonResponse({'success': 'Todo deleted successfully'})
    except Todolist.DoesNotExist:
        return JsonResponse({'error': 'Todo not found'})
    
    
    
    
@api_view(['PUT','GET'])
def updateTodo(request,id): 
    todo = Todolist.objects.get(id =id)
    if request.method =="PUT": 
        
        serializers = TodolistSerializer(todo,data = request.data)
        if serializers.is_valid(): 
            serializers.save()
            return Response({'data':"data updated successfully",'data':serializers.data})
        return Response({'error':"data not updated"})
    
    serializers = TodolistSerializer(todo)
    
    return Response(serializers.data)

        

        