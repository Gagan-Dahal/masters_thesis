from django.urls import path
from . import views

urlpatterns = [
    path('',views.StdDashboardView.as_view(),name="sdashboard"),
    path('upload/',views.upload,name="suploadthesis"),
    path('addrev/',views.addrevised,name="saddrev"),
]
