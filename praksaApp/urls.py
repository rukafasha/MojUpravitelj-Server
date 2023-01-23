from django.urls import path
from .Models.Role.RoleView import RoleGetAll, RoleAdd, RoleGetById, RolePut, RoleDelete
from .Models.RolePerson.RolePersonView import RolePersonGetAll, RolePersonAdd, RolePersonGetById, RolePersonPut, RolePersonDelete
from .Models.UserAccount.UserAccountView import UserAccountGetAll, UserAccountAdd, UserAccountGetById, UserAccountPut, UserAccountDelete
from .Models.Person.PersonView import PersonGetAll, PersonAdd, PersonGetById, PersonPut, PersonDelete

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
]