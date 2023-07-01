from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('calculate/',views.calculate, name='calculate'),
    path('calculate/result/', views.result, name='result'),
    path('calculate/result/aboveaverage', views.result, name='aboavg'),
    path('calculate/result/belaverage', views.result, name='belavg'),
    path('chat/', views.chat_view, name='chat_view')
]