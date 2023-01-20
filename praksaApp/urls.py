from django.urls import path
from .Models.Role.RoleView import RoleList, RoleDetail
from .Models.RolePerson.RolePersonView import RolePersonList, RolePersonDetail
from .Models.UserAccount.UserAccountView import UserAccountList, UserAccountDetail
from .Models.Person.PersonView import PersonList, PersonDetail

urlpatterns = [
    path('role/', RoleList),
    path('role/<int:id>', RoleDetail),
    path('role-person/', RolePersonList),
    path('role-person/<int:id>', RolePersonDetail),
    path('person/', UserAccountList),
    path('person/<int:id>', UserAccountDetail),
    path('user-account/', PersonList),
    path('user-account/<int:id>', PersonDetail),
]