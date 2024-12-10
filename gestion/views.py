from django.shortcuts import render

def index(request):
    return render(request, 'index.html') 

def doctores(request):
    return render(request, 'doctores.html')  

def pacientes(request):
    return render(request, 'pacientesCitas.html')  
    from django.shortcuts import render

