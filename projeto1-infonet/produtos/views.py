from django.shortcuts import render
from .models import Produto

# Create your views here.
def listar(request):
    # SELECT * FROM produtos_produto;
    produtos = Produto.objects.all()
    return render(request, 'produtos/pages/listar.html', {'produto': produtos})

def cadastrar(request):
    return render(request, 'produtos/pages/cadastrar.html')
