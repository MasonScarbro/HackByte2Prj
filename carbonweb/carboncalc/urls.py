from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('result/', views.result, name='result'),
    path('result/aboveaverage', views.result, name='aboavg'),
    path('result/belaverage', views.result, name='belavg')
]