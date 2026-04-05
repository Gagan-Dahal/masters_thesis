from django.urls import path
from . import views

urlpatterns = [
    path('', views.thesis_list, name='thesis_list'),
    path('thesis/<int:id>/',
         views.thesis_detail,
         name='thesis_detail'),
    path('evaluate/<int:id>/',
         views.evaluate_thesis,
         name='evaluate_thesis'),
]
