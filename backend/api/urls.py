#this is sperate to the rest of the application 
from django.urls import path
from . import views
#from .views import api_home

#these need to be brought into, or are brought into the main urls file.
urlpatterns = [
    path('', views.api_home)
]