from .Models.Appartment.AppartmentView import AppartmentGetAll, AppartmentAdd, AppartmentGetById, AppartmentPut, AppartmentDelete
from .Models.AppartmentPerson.AppartmentPersonView import AppartmentPersonGetAll, AppartmentPersonAdd, AppartmentPersonGetById, AppartmentPersonPut, AppartmentPersonDelete
from .Models.Comment.CommentView import CommentGetAll, CommentAdd, CommentGetById, CommentPut, CommentDelete
from .Models.Report.ReportView import ReportGetAll, ReportAdd, ReportGetById, ReportPut, ReportDelete
from .Models.ReportStatus.ReportStatusView import ReportStatusGetAll, ReportStatusAdd, ReportStatusGetById, ReportStatusPut, ReportStatusDelete
from django.urls import path

urlpatterns = [
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