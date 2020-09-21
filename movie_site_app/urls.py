from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('jmoore_test_route/', views.jmoore_test)
]