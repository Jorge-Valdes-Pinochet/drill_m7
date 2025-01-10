from django.shortcuts import render, get_object_or_404, redirect
from .models import Laboratorio

# Vista para mostrar la lista de laboratorios
def laboratorio_list(request):
    laboratorios = Laboratorio.objects.all()  # Obtiene todos los laboratorios
    return render(request, 'laboratorio/laboratorio_list.html', {'laboratorios': laboratorios})

# Vista para mostrar el detalle de un laboratorio
def laboratorio_detail(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)  # Busca el laboratorio por su clave primaria (ID)
    return render(request, 'laboratorio/laboratorio_detail.html', {'laboratorio': laboratorio})

# Vista para crear un laboratorio
def laboratorio_create(request):
    if request.method == 'POST':  # Si el formulario fue enviado
        nombre = request.POST.get('nombre')  # Obtiene el valor del campo 'nombre'
        Laboratorio.objects.create(nombre=nombre)  # Crea el laboratorio en la base de datos
        return redirect('laboratorio_list')  # Redirige a la lista de laboratorios
    return render(request, 'laboratorio/laboratorio_form.html')  # Muestra el formulario

# Vista para editar un laboratorio
def laboratorio_edit(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)  # Busca el laboratorio
    if request.method == 'POST':  # Si el formulario fue enviado
        laboratorio.nombre = request.POST.get('nombre')  # Actualiza el nombre
        laboratorio.save()  # Guarda los cambios
        return redirect('laboratorio_list')  # Redirige a la lista de laboratorios
    return render(request, 'laboratorio/laboratorio_form.html', {'laboratorio': laboratorio})  # Muestra el formulario

# Vista para eliminar un laboratorio
def laboratorio_delete(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)  # Busca el laboratorio
    if request.method == 'POST':  # Si el formulario fue enviado
        laboratorio.delete()  # Elimina el laboratorio
        return redirect('laboratorio_list')  # Redirige a la lista de laboratorios
    return render(request, 'laboratorio/laboratorio_confirm_delete.html', {'laboratorio': laboratorio})  # Confirma eliminación
