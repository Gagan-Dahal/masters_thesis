from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard,name="sdashboard"),
    path('upload/',views.upload,name="suploadthesis"),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
