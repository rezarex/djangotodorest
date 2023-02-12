from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.apiOverview,),

    path('todo/', include([
        path('list/', views.todoList),
        path('detail/<str:pk>/', views.todoDetail),
        path('create/', views.todoCreate),
        path('update/<str:pk>/', views.todoUpdate),
        path('delete/<str:pk>/', views.todoDelete),
    ]))

]

