from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home, name='adminInstitutionHome'),
    path('ProgramCoordinatorList/', views.coordinator_list, name='CoordinatorList'),
    path('ProgramList/', views.program_list, name='ProgramList'),
    path('logout/', views.logout_user, name='logout'),

]