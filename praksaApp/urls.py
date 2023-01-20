from django.urls import path
from .Models.Country.CountryView import CountryGetAll, CountryAdd, CountryDelete,CountryGetByID,CountryPut
from .Models.County.CountyView import CountyPut, CountyAdd, CountyDelete, CountyGetAll, CountyGetByID
from .Models.Building.BuildingView import BuildingAdd, BuildingPut, BuildingDelete, BuildingGetAll, BuildingGetByID
from .Models.Company.CompanyView import CompanyAdd, CompanyDelete, CompanyGetAll, CompanyGetByID,CompanyPut

urlpatterns = [
    path('country/', CountryGetAll),
    path('country/post/', CountryAdd),
    path('country/delete/<int:id>/', CountryGetByID),
    path('country/delete/<int:id>/', CountryPut),
    path('country/delete/<int:id>/', CountryDelete),
    path('county/', CountyGetAll),
    path('county/post/', CountyAdd),
    path('county/<int:id>/', CountyGetByID),
    path('county/put/<int:id>/', CountyPut),
    path('county/delete/<int:id>/', CountyDelete),
    path('building/', BuildingGetAll),
    path('building/post/', BuildingAdd),
    path('building/<int:id>/', BuildingGetByID),
    path('building/put/<int:id>/', BuildingPut),
    path('building/delete/<int:id>/', BuildingDelete),
    path('company/', CompanyGetAll),
    path('company/post/', CompanyAdd),
    path('company/<int:id>/', CompanyGetByID),
    path('company/put/<int:id>/', CompanyPut),
    path('company/delete/<int:id>/', CompanyDelete),
]
