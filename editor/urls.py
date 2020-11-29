from django.urls import path
from . import views

urlpatterns = [
    path('creater/', views.creater, name='ecreater'),
]
