from django.shortcuts import render

# Create your views here.

def index(request):
    context ={
        'name': 'Pedro',
        'apellido': 'Diaz',
        'cursos': ['Django', 'javascript', 'c#']
    }
    return render(request, 'index.html', context)