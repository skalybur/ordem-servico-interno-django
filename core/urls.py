from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views # Importe as views de autenticação

urlpatterns = [
    path('admin/', admin.site.urls),
    # Rotas de Autenticação (Requisito obrigatório)
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('', include('ordem_servico.urls')),
]