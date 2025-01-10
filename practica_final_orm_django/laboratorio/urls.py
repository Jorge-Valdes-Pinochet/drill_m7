from django.urls import path
from . import views

urlpatterns = [
    path('', views.laboratorio_list, name='laboratorio_list'),  # Lista de laboratorios
    path('<int:pk>/', views.laboratorio_detail, name='laboratorio_detail'),  # Detalle de laboratorio
    path('create/', views.laboratorio_create, name='laboratorio_create'),  # Crear laboratorio
    path('<int:pk>/edit/', views.laboratorio_edit, name='laboratorio_edit'),  # Editar laboratorio
    path('<int:pk>/delete/', views.laboratorio_delete, name='laboratorio_delete'),  # Eliminar laboratorio
]
