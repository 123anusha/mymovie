from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signup,name='vsup'),
    path('login/',views.login,name='vlog'),
    path('logout/',views.logout,name='vout'),
]