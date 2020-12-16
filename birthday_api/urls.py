from django.urls import path
from . import views

urlpatterns = [
	path('person-list/', views.personList, name="person-list"),
]
