from django.urls import path
from . import views

urlpatterns = [
    path('', views.inscription_view, name='inscription'),
    path('confirmation/<int:pk>/', views.confirmation_view, name='confirmation'),
    path('recu/<int:pk>/', views.generer_recu_pdf, name='recu_pdf'),
]
