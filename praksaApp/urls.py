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
from django.urls import path
from .Models.Role.RoleView import RoleGetAll, RoleAdd, RoleGetById, RolePut, RoleDelete
from .Models.RolePerson.RolePersonView import RolePersonGetAll, RolePersonAdd, RolePersonGetById, RolePersonPut, RolePersonDelete
from .Models.UserAccount.UserAccountView import UserAccountGetAll, UserAccountAdd, UserAccountGetById, UserAccountPut, UserAccountDelete
from .Models.Person.PersonView import PersonGetAll, PersonAdd, PersonGetById, PersonPut, PersonDelete
from .Models.Appartment.AppartmentView import AppartmentGetAll, AppartmentAdd, AppartmentGetById, AppartmentPut, AppartmentDelete
from .Models.AppartmentPerson.AppartmentPersonView import AppartmentPersonGetAll, AppartmentPersonAdd, AppartmentPersonGetById, AppartmentPersonPut, AppartmentPersonDelete
from .Models.Comment.CommentView import CommentGetAll, CommentAdd, CommentGetById, CommentPut, CommentDelete
from .Models.Report.ReportView import ReportGetAll, ReportAdd, ReportGetById, ReportPut, ReportDelete
from .Models.ReportStatus.ReportStatusView import ReportStatusGetAll, ReportStatusAdd, ReportStatusGetById, ReportStatusPut, ReportStatusDelete

urlpatterns = [
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
    
    path('userAccount/', UserAccountGetAll),
    path('userAccount/add', UserAccountAdd),
    path('userAccount/<int:id>', UserAccountGetById),
    path('userAccount/edit/<int:id>', UserAccountPut),
    path('userAccount/delete/<int:id>', UserAccountDelete),
    
    path('person/', PersonGetAll),
    path('person/add', PersonAdd),
    path('person/<int:id>', PersonGetById),
    path('person/edit/<int:id>', PersonPut),
    path('person/delete/<int:id>', PersonDelete),

    path('appartment/', AppartmentGetAll),
    path('appartment/add', AppartmentAdd),
    path('appartment/<int:id>', AppartmentGetById),
    path('appartment/edit/<int:id>', AppartmentPut),
    path('appartment/delete/<int:id>', AppartmentDelete),

    path('appartmentPerson/', AppartmentPersonGetAll),
    path('appartmentPerson/add', AppartmentPersonAdd),
    path('appartmentPerson/<int:id>', AppartmentPersonGetById),
    path('appartmentPerson/edit/<int:id>', AppartmentPersonPut),
    path('appartmentPerson/delete/<int:id>', AppartmentPersonDelete),
    
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
    

    path('reportStatus/', ReportStatusGetAll),
    path('reportStatus/add', ReportStatusAdd),
    path('reportStatus/<int:id>', ReportStatusGetById),
    path('reportStatus/edit/<int:id>', ReportStatusPut),
    path('reportStatus/delete/<int:id>', ReportStatusDelete),
]