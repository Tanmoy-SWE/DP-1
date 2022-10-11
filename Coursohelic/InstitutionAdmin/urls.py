from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.login, name='login'),
    path('AdminRegistrationPage/',views.registration, name="AdminRegistrationPage"),
    # path('courseInstructorForm/', views.cour_ins_form, name='courseInstructorForm'),
    # path('coordinatorForm/', views.coordinator, name='coordinatorForm'),
]