from django.urls import path
from . import views

urlpatterns = [
	path('', views.get_students, name='get_students'),
	path('create/', views.post_student, name='post_student'),
]
