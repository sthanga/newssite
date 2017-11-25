from django.urls import path, include
from newsapp import views
#sfrom newsapp import feed

urlpatterns = [
	path ('', views.index),
]