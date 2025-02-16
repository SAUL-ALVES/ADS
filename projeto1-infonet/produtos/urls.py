from django.urls import path
from .views import listar, cadastrar

urlpatterns = [
    path('', listar, name='listar'),
    path('cadastrar/', cadastrar, name='cadastrar'),
]
