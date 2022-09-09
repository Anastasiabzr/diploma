from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('result/', views.result, name="result"),
    path('ege/', views.ege, name="ege"),
    path('<int:pk>/', views.test, name="test"),
    path('<int:pk>/ans/', views.next_question, name="next_quest"),
    path('info/', views.info, name='info')
]
