from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.login, name='login'),
    path('AdminRegistrationPage/', views.auth, name='auth'),
    path('AdminHome/',views.home, name='home')
]