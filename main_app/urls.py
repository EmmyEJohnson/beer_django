from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
# path('route string', name of view function, name="string name of route")
path('', views.Home.as_view(), name="home"),
path('about/', views.About.as_view(), name="about"),
path('beers/', views.BeerList.as_view(), name="beer_list"),
path('beers/new/', views.BeerCreate.as_view(), name="beer_create"),
path('beers/<int:pk>/', views.BeerDetail.as_view(), name="beer_detail"),
path('beers/<int:pk>/update',
         views.BeerUpdate.as_view(), name="beer_update"),
path('beers/<int:pk>/delete',
         views.BeerDelete.as_view(), name="beer_delete_confirm"),
]
