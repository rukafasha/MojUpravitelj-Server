from django.urls import path
from .Models.Country.CountryView import CountryGetAll, CountryAdd, CountryDelete,CountryGetByID,CountryPut
from .Models.County.CountyView import CountyPut, CountyAdd, CountyDelete, CountyGetAll, CountyGetByID
from .Models.Building.BuildingView import BuildingAdd, BuildingPut, BuildingDelete, BuildingGetAll, BuildingGetByID
from .Models.Company.CompanyView import CompanyAdd, CompanyDelete, CompanyGetAll, CompanyGetByID,CompanyPut

urlpatterns = [
    path('country/', CountryGetAll),
    path('country/add', CountryAdd),
    path('country/<int:id>', CountryGetByID),
    path('country/edit/<int:id>', CountryPut),
    path('country/delete/<int:id>', CountryDelete),
    
    path('county/', CountyGetAll),
    path('county/add', CountyAdd),
    path('county/<int:id>', CountyGetByID),
    path('county/edit/<int:id>', CountyPut),
    path('county/delete/<int:id>', CountyDelete),
    
    path('building/', BuildingGetAll),
    path('building/add', BuildingAdd),
    path('building/<int:id>', BuildingGetByID),
    path('building/edit/<int:id>', BuildingPut),
    path('building/delete/<int:id>', BuildingDelete),
    
    path('company/', CompanyGetAll),
    path('company/add', CompanyAdd),
    path('company/<int:id>', CompanyGetByID),
    path('company/edit/<int:id>', CompanyPut),
    path('company/delete/<int:id>', CompanyDelete),
]
