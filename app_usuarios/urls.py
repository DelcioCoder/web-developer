from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name = 'app_usuarios'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='app_usuarios/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/',views.registro, name='registro'),
]