from django.shortcuts import render, redirect
from inicio.models import User
from inicio.forms import CrearUserFormulario


def inicio(request):
    return render(request, 'inicio/index.html')

def crear_user(request):
    
    print('Valor de la request: ', request)
    print('Valor de GET: ', request.GET)
    print('Valor de POST: ', request.POST)
    
    formulario = CrearUserFormulario()
    
    if request.method == 'POST':
        formulario = CrearUserFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            user = User(nombre=datos.get('nombre'), apellido=datos.get('apellido'), edad=datos.get('edad'))
            user.save()
            return redirect('user')

    return render(request, 'inicio/crear_user.html', {'formulario': formulario})

def user(request):
    
    user = User.objects.all()
    
    return render(request, 'inicio/user.html', {'user': user})