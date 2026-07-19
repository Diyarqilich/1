from django.urls import path
from .views import *

urlpatterns = [
    path("cats/", CatsListView),
    path("cats/<int:pk>/", CatsDetailView),
    path("cats/create/", CatsCreateView),
    path("cats/update/<int:pk>/", CatsUpdateView),
    path("cats/delete/<int:pk>/", CatsDeleteView),
]