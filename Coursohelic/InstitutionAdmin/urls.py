from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home, name='home'),
    path('ProgramCoordinatorList/', views.coordinator_list, name='CoordinatorList'),
    path('ProgramList/', views.program_list, name='ProgramList'),
]