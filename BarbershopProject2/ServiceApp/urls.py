from django.urls import path
from ServiceApp import views

urlpatterns = [
    path('service/', views.serviceApi),
    path('service/<int:id>', views.serviceApi),
]
