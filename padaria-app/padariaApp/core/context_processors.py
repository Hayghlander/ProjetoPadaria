# coding=utf-8

from .models import Categoria

def categories(request):
    return {
        'categories': Categoria.objects.all()
    }
