from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("home/", views.home),
    path("oNas/", views.oNas),
    path("oProjekcie/", views.oProjekcie),
    path("kontakt/", views.kontakt),
    path("dokumenty/", views.dokumenty),
    path("spotkania/", views.spotkania),
    path("galeria/", views.galeria)
]
