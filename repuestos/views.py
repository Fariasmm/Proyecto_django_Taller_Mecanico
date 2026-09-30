from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib import messages
from .models import Repuesto
from .forms import RepuestoForm

# LISTAR Y BUSCAR (ORM) - Accesible para cualquier usuario
def catalogo_repuestos(request):
    query = request.GET.get('q', '').strip()
    if query:
        repuestos = Repuesto.objects.filter(
            nombre__icontains=query
        ) | Repuesto.objects.filter(
            categoria__icontains=query
        ) | Repuesto.objects.filter(
            codigo__icontains=query
        )
    else:
        repuestos = Repuesto.objects.all()

    return render(request, 'repuestos/catalogo.html', {
        'repuestos': repuestos,
        'total_items': repuestos.count(),
        'busqueda': query
    })

# AGREGAR REPUESTO - Requiere permiso "Can add Repuesto"
@permission_required('repuestos.add_repuesto', login_url='repuestos_catalogo', raise_exception=False)
def repuesto_crear(request):
    if request.method == 'POST':
        form = RepuestoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Repuesto agregado con éxito.')
            return redirect('repuestos_catalogo')
    else:
        form = RepuestoForm()
    return render(request, 'repuestos/repuesto_form.html', {
        'form': form, 
        'titulo': 'Agregar Nuevo Repuesto'
    })

# EDITAR REPUESTO - Requiere permiso "Can change Repuesto"
@permission_required('repuestos.change_repuesto', login_url='repuestos_catalogo', raise_exception=False)
def repuesto_editar(request, id):
    repuesto = get_object_or_404(Repuesto, id=id)
    if request.method == 'POST':
        form = RepuestoForm(request.POST, request.FILES, instance=repuesto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Repuesto actualizado correctamente.')
            return redirect('repuestos_catalogo')
    else:
        form = RepuestoForm(instance=repuesto)
    return render(request, 'repuestos/repuesto_form.html', {
        'form': form, 
        'titulo': 'Modificar Repuesto'
    })

# ELIMINAR REPUESTO - Requiere permiso "Can delete Repuesto"
@permission_required('repuestos.delete_repuesto', login_url='repuestos_catalogo', raise_exception=False)
def repuesto_eliminar(request, id):
    repuesto = get_object_or_404(Repuesto, id=id)
    if request.method == 'POST':
        repuesto.delete()
        messages.success(request, 'Repuesto eliminado del sistema.')
        return redirect('repuestos_catalogo')
    return render(request, 'repuestos/repuesto_confirmar_eliminar.html', {
        'repuesto': repuesto
    })

# COTIZADOR (ORM)
def cotizador_repuestos(request):
    repuestos = Repuesto.objects.all()
    precios = [r.precio for r in repuestos]
    promedio = sum(precios) / len(precios) if precios else 0

    return render(request, 'repuestos/cotizador.html', {
        'repuestos': repuestos,
        'precio_promedio': int(promedio)
    })