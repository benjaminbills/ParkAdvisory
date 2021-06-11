from django.urls import path
from . import views


urlpatterns = [
   path('', views.home, name='home' ),
   path('add_park/', views.addPark, name='add_park'),
   path('get_parks/', views.getParks, name='get_parks'),

]
