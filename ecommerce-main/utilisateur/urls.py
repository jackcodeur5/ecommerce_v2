
from django.urls import path
from . import views


urlpatterns = [
    path('inscription', views.inscription, name="inscription"),
    path('access', views.access, name="access"),
    path('index', views.index, name="index"),
    path('recu', views.recu, name="recu"),
    path('recu-pdf/<str:pk>', views.recu_pdf, name="recu_pdf"),
    path('quitter', views.quitter, name="quitter"),
    path('tester', views.test, name="test"),
]

"""
from .views import RegisterAPI
from django.urls import path

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('allutilisateur/', views.allUtilisateurs),
    path('getutilisateur/<int:id>/', views.getUtilisateur),
    path('addutilisateur/', views.addUtilisateur),
    path('updateutilisateur/<int:id>/', views.updateUtilisateur),
    path('deleteutilisateur/<int:id>/', views.deleteUtilisateur),
    #path('login/', views.login_api),
]
"""