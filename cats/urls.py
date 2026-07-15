from django.urls import path
from . import views

urlpatterns = [
    path("cats/", views.CatListViewSet.as_view(), name="cat-list"),
    path("cats/create/", views.CatCreateViewSet.as_view(), name="cat-create"),
    path("cats/<int:pk>/", views.CatRetrieveViewSet.as_view(), name="cat-detail"),
    path("cats/<int:pk>/update/", views.CatUpdateViewSet.as_view(), name="cat-update"),
    path("cats/<int:pk>/delete/", views.CatDestroyViewSet.as_view(), name="cat-delete"),
    path("cats/<int:pk>/update-destroy/", views.CatRetrieveUpdateDestroyViewSet.as_view(), name="cat-update-destroy"),
]