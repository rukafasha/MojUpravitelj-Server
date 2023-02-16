from django.contrib import admin
from .Models.Appartment.AppartmentModel import *
from .Models.Building.BuildingModel import *
from .Models.AppartmentPerson.AppartmentPersonModel import *
from .Models.Comment.CommentModel import *
from .Models.Company.CompanyModel import *
from .Models.Country.CountryModel import *
from .Models.County.CountyModel import *
from .Models.Person.PersonModel import *
from .Models.Report.ReportModel import *
from .Models.ReportStatus.ReportStatusModel import *
from .Models.Role.RoleModel import *
from .Models.UserAccount.UserAccountModel import *
from .Models.RolePerson.RolePersonModel import *
from .Models.Request.RequestModel import *

# Register your models here.

admin.site.register(Appartment)
admin.site.register(AppartmentPerson)
admin.site.register(Building)
admin.site.register(Comment)
admin.site.register(Company)
admin.site.register(Country)
admin.site.register(County)
admin.site.register(Person)
admin.site.register(Report)
admin.site.register(ReportStatus)
admin.site.register(Role)
admin.site.register(RolePerson)
admin.site.register(UserAccount)
admin.site.register(Request)
