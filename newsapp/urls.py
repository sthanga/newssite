from django.urls import path, include
from newsapp import views

urlpatterns = [
	path ('', views.index),
]