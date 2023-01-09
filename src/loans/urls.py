from django.urls import path

from . import views

urlpatterns = [
    path("loans/", views.loans_list, name="loan-list"),
    path("countries/", views.country_list, name="loan-countries-list"),
    path("sectors/", views.SectorList.as_view(), name="loan-sectors-list"),
]
