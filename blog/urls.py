from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('test', views.test, name='test'),
    path('bankregister', views.bankregister, name='bankregister'),
    path('pbankregister', views.pbankregister, name='pbankregister'),
    path('pbbankregister', views.pbbankregister, name='pbbankregister'),
    path('bankdashboard', views.bankdashboard, name='bankdashboard'),
   
]
