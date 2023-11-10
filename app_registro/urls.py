from django.urls import path
from . import views 
app_name = 'app_registro'

urlpatterns = [
    path('', views.index, name='index'),
    path('topicos/', views.topicos, name='topicos'),
    path('topicos/<int:topico_id>/', views.topico, name='topico'),
    path('novo_topico/', views.novo_topico, name='novo_topico'),
    path('nova_entrada/<int:topico_id>/', views.nova_entrada, name='nova_entrada'),
    path('editar_entrada/<int:entrada_id>/', views.editar_entrada, name='editar_entrada'),
]