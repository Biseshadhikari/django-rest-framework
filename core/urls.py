
from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name = "index"),
    path("home/",home,name = "home"),
    path('createTodo',createTodo),
    path('updateTodo/<int:id>/',updateTodo),
    path('deleteTodo/<int:id>/', deleteTodo),  # Add this line

]
