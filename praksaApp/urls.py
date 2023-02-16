from django.urls import path

from praksaApp.Auth.AuthView import CompanyRegistration, Login, Registration
from praksaApp.Models.Request.RequestView import RequestGetAll, RequestGetNotApproved, RequestPut

from .Models.Country.CountryView import CountryGetAll, CountryAdd, CountryDelete,CountryGetByID,CountryPut
from .Models.County.CountyView import CountyPut, CountyAdd, CountyDelete, CountyGetAll, CountyGetByID, getCountyByCountry, getCountyByName
from .Models.Building.BuildingView import BuildingAdd, BuildingPut, BuildingDelete, BuildingGetAll, BuildingGetByID, GetBuildingByUser,GetBuildingByCompany, GetBuildingsByAddress
from .Models.Company.CompanyView import CompanyAdd, CompanyDelete, CompanyGetAll, CompanyGetByID,CompanyPut
from .Models.Role.RoleView import RoleGetAll, RoleAdd, RoleGetById, RolePut, RoleDelete
from .Models.RolePerson.RolePersonView import RolePersonGetAll, RolePersonAdd, RolePersonGetById, RolePersonPut, RolePersonDelete, RoleGetByUser
from .Models.UserAccount.UserAccountView import UserAccountGetAll, UserAccountAdd, UserAccountGetById, UserAccountPut, UserAccountDelete, UserAccountUsernameVerification
from .Models.Person.PersonView import PersonGetAll, PersonAdd, PersonGetById, PersonPut, PersonDelete, GetPersonByAppartment
from .Models.Appartment.AppartmentView import AppartmentGetAll, AppartmentAdd, AppartmentGetById, AppartmentPut, AppartmentDelete
from .Models.AppartmentPerson.AppartmentPersonView import AppartmentPersonGetAll, AppartmentPersonAdd, AppartmentPersonGetById, AppartmentPersonPut, AppartmentPersonDelete, GetApartmentsByBuildingId, GetApartmentsByPersonId
from .Models.Comment.CommentView import CommentGetAll, CommentAdd, CommentGetById, CommentPut, CommentDelete
from .Models.Report.ReportView import ReportGetAll, ReportAdd, ReportGetById, ReportPut, ReportDelete, ReportGetByUser, ReportGetByCompany, ReportGetByBuilding
from .Models.ReportStatus.ReportStatusView import ReportStatusGetAll, ReportStatusAdd, ReportStatusGetById, ReportStatusPut, ReportStatusDelete


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
    path('county/country/<str:string>', getCountyByCountry),
    path('county/<str:string>', getCountyByName),
    
    path('building/', BuildingGetAll),
    path('building/add', BuildingAdd),
    path('building/<int:id>', BuildingGetByID),
    path('building/edit/<int:id>', BuildingPut),
    path('building/delete/<int:id>', BuildingDelete),
    path('building/get/user/<int:id>', GetBuildingByUser),
    path('building/get/company/<int:id>', GetBuildingByCompany),
    path('building/details/<str:address>', GetBuildingsByAddress),

    
    path('company/', CompanyGetAll),
    path('company/add', CompanyAdd),
    path('company/<int:id>', CompanyGetByID),
    path('company/edit/<int:id>', CompanyPut),
    path('company/delete/<int:id>', CompanyDelete),

    path('role/', RoleGetAll),
    path('role/add', RoleAdd),
    path('role/<int:id>', RoleGetById),
    path('role/edit/<int:id>', RolePut),
    path('role/delete/<int:id>', RoleDelete),
    
    path('rolePerson/', RolePersonGetAll),
    path('rolePerson/add', RolePersonAdd),
    path('rolePerson/<int:id>', RolePersonGetById),
    path('rolePerson/edit/<int:id>', RolePersonPut),
    path('rolePerson/delete/<int:id>', RolePersonDelete),
    path('rolePerson/get/user/<int:id>', RoleGetByUser),
    
    path('userAccount/', UserAccountGetAll),
    path('userAccount/add', UserAccountAdd),
    path('userAccount/<int:id>', UserAccountGetById),
    path('userAccount/edit/<int:id>', UserAccountPut),
    path('userAccount/delete/<int:id>', UserAccountDelete),
    path('userAccount/username/<str:username>', UserAccountUsernameVerification),
    
    path('person/', PersonGetAll),
    path('person/add', PersonAdd),
    path('person/<int:id>', PersonGetById),
    path('person/edit/<int:id>', PersonPut),
    path('person/delete/<int:id>', PersonDelete),
    path('person/get/apartment/<int:id>', GetPersonByAppartment),

    path('appartment/', AppartmentGetAll),
    path('appartment/add', AppartmentAdd),
    path('appartment/<int:id>', AppartmentGetById),
    path('appartment/edit/<int:id>', AppartmentPut),
    path('appartment/delete/<int:id>', AppartmentDelete),
    path('appartment/details/<int:id>', GetApartmentsByBuildingId),

    path('appartmentPerson/', AppartmentPersonGetAll),
    path('appartmentPerson/add', AppartmentPersonAdd),
    path('appartmentPerson/<int:id>', AppartmentPersonGetById),
    path('appartmentPerson/edit/<int:id>', AppartmentPersonPut),
    path('appartmentPerson/delete/<int:id>', AppartmentPersonDelete),
    path('appartmentPerson/person/<int:id>', GetApartmentsByPersonId),
    
    path('comment/', CommentGetAll),
    path('comment/add', CommentAdd),
    path('comment/<int:id>', CommentGetById),
    path('comment/edit/<int:id>', CommentPut),
    path('comment/delete/<int:id>', CommentDelete),

    path('report/', ReportGetAll),
    path('report/add', ReportAdd),
    path('report/<int:id>', ReportGetById),
    path('report/edit/<int:id>', ReportPut),
    path('report/delete/<int:id>', ReportDelete),
    path('report/get/user/<int:id>', ReportGetByUser),
    path('report/get/building', ReportGetByBuilding),
    path('report/get/company/<int:id>', ReportGetByCompany),
    
    path('reportStatus/', ReportStatusGetAll),
    path('reportStatus/add', ReportStatusAdd),
    path('reportStatus/<int:id>', ReportStatusGetById),
    path('reportStatus/edit/<int:id>', ReportStatusPut),
    path('reportStatus/delete/<int:id>', ReportStatusDelete),

    path('request/', RequestGetAll),
    path('request/notApproved/<int:id>', RequestGetNotApproved),
    path('request/edit/<int:id>', RequestPut),

    path('registration', Registration),
    path('companyRegistration', CompanyRegistration),
    path('login', Login),
] 