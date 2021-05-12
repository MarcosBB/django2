from django.shortcuts import render

def index (request):
    return render(request, 'index.html')

def contato (request):
    return render(request, 'contato.html')

def produto (request):
    return render(request, 'produto.html')
