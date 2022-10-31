from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home, name='adminInstitutionHome'),
    path('ProgramCoordinatorList/', views.coordinator_list, name='CoordinatorList'),
    path('ProgramList/', views.program_list, name='ProgramList'),
    path('ProgramList/AddProgram/', views.add_program, name='add_program'),
    path('logout/', views.logout_user, name='logout'),
    path('ProgramList/Delete_Program/<pk>', views.delete_program, name='delete_program'),
    path('ProgramCoordinatorList/addCoordinator/',views.addCoordinator, name='addCoordinator'),
    path('ProgramCoordinatorList/addCoordinator/assignCoordinator/<pk>/', views.assignCoordinator, name='assignCoordinator'),
    path('DeAssignCoordinator/<pk>/', views.deassign_coordinator, name='deassign_coordinator'),
    path('coordinator_confirmation/<pk>/', views.coordinator_confirmation, name='coordinator_confirmation'),
    path('go_back', views.go_back, name="go_back"),
    path('program_confirmation/<pk>/', views.program_confirmation, name="program_confirmation"),
    path('go_back_program', views.go_back_program,  name="go_back_program")
    
]