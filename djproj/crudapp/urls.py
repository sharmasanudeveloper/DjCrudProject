from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('addstu/',views.addstudent),
    path('del-std/<int:id>',views.delete),
    path('update-std/<int:id>',views.updat),
]