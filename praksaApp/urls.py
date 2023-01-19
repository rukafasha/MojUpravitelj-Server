from django.urls import path
from .Models.Country.CountryView import CountryList, CountryDetail
from .Models.County.CountyView import CountyList, CountyDetail
from .Models.Building.BuildingView import BuildingList, BuildingDetail
from .Models.Company.CompanyView import CompanyList, CompanyDetail

urlpatterns = [
    path('country/', CountryList),
    path('country/<int:id>', CountryDetail),
    path('county/', CountyList),
    path('county/<int:id>', CountyDetail),
    path('building/', BuildingList),
    path('building/<int:id>', BuildingDetail),
    path('company/', CompanyList),
    path('company/<int:id>', CompanyDetail),
]
