from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib import messages
from .models import ServicioMantenimiento, OrdenTrabajo
from .forms import ServicioMantenimientoForm, OrdenTrabajoForm

# INICIO DEL TALLER
def inicio_mantenimiento(request):
    return render(request, 'mantenimiento/inicioM.html', {
        'titulo': 'Centro de Servicios Mecánicos'
    })

# LISTAR Y BUSCAR SERVICIOS (ORM)
def lista_servicios(request):
    query = request.GET.get('q', '').strip()
    if query:
        servicios_resultado = ServicioMantenimiento.objects.filter(
            nombre__icontains=query
        ) | ServicioMantenimiento.objects.filter(
            descripcion__icontains=query
        )
    else:
        servicios_resultado = ServicioMantenimiento.objects.all()

    return render(request, 'mantenimiento/servicios.html', {
        'servicios': servicios_resultado,
        'total_servicios': servicios_resultado.count(),
        'busqueda': query
    })

# AGREGAR SERVICIO - Requiere permiso "Can add Servicio de Mantenimiento"
@permission_required('mantenimiento.add_serviciomantenimiento', login_url='mantenimiento_servicios', raise_exception=False)
def servicio_crear(request):
    if request.method == 'POST':
        form = ServicioMantenimientoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Servicio de mantenimiento registrado exitosamente.')
            return redirect('mantenimiento_servicios')
    else:
        form = ServicioMantenimientoForm()
    return render(request, 'mantenimiento/servicio_form.html', {
        'form': form, 
        'titulo': 'Agregar Servicio'
    })

# EDITAR SERVICIO - Requiere permiso "Can change Servicio de Mantenimiento"
@permission_required('mantenimiento.change_serviciomantenimiento', login_url='mantenimiento_servicios', raise_exception=False)
def servicio_editar(request, id):
    servicio = get_object_or_404(ServicioMantenimiento, id=id)
    if request.method == 'POST':
        form = ServicioMantenimientoForm(request.POST, request.FILES, instance=servicio)
        if form.is_valid():
            form.save()
            messages.success(request, 'Servicio modificado exitosamente.')
            return redirect('mantenimiento_servicios')
    else:
        form = ServicioMantenimientoForm(instance=servicio)
    return render(request, 'mantenimiento/servicio_form.html', {
        'form': form, 
        'titulo': 'Modificar Servicio'
    })

# ELIMINAR SERVICIO - Requiere permiso "Can delete Servicio de Mantenimiento"
@permission_required('mantenimiento.delete_serviciomantenimiento', login_url='mantenimiento_servicios', raise_exception=False)
def servicio_eliminar(request, id):
    servicio = get_object_or_404(ServicioMantenimiento, id=id)
    if request.method == 'POST':
        servicio.delete()
        messages.success(request, 'Servicio eliminado correctamente.')
        return redirect('mantenimiento_servicios')
    return render(request, 'mantenimiento/servicio_confirmar_eliminar.html', {
        'servicio': servicio
    })

# ----------------- TRANSACCIÓN: ÓRDENES DE TRABAJO ----------------- #

# LISTAR ÓRDENES - Requiere permiso "Can view Orden de Trabajo"
@permission_required('mantenimiento.view_ordentrabajo', login_url='mantenimiento_inicio', raise_exception=False)
def ordenes_listar(request):
    query = request.GET.get('q', '').strip()
    if query:
        ordenes = OrdenTrabajo.objects.filter(
            patente_moto__icontains=query
        ) | OrdenTrabajo.objects.filter(
            cliente_nombre__icontains=query
        )
    else:
        ordenes = OrdenTrabajo.objects.all().order_by('-fecha')

    return render(request, 'mantenimiento/ordenes_listar.html', {
        'ordenes': ordenes,
        'query': query
    })

# CREAR ÓRDEN - Requiere permiso "Can add Orden de Trabajo"
@permission_required('mantenimiento.add_ordentrabajo', login_url='ordenes_listar', raise_exception=False)
def orden_crear(request):
    if request.method == 'POST':
        form = OrdenTrabajoForm(request.POST)
        if form.is_valid():
            orden = form.save()
            messages.success(request, f'Orden de Trabajo #{orden.id} creada exitosamente por un total de ${orden.total}.')
            return redirect('ordenes_listar')
    else:
        form = OrdenTrabajoForm()
    return render(request, 'mantenimiento/orden_form.html', {
        'form': form, 
        'titulo': 'Registrar Nueva Orden de Trabajo'
    })

# EDITAR ÓRDEN DE TRABAJO - Requiere permiso "Can change Orden de Trabajo"
@permission_required('mantenimiento.change_ordentrabajo', login_url='ordenes_listar', raise_exception=False)
def orden_editar(request, id):
    orden = get_object_or_404(OrdenTrabajo, id=id)
    if request.method == 'POST':
        form = OrdenTrabajoForm(request.POST, instance=orden)
        if form.is_valid():
            orden_actualizada = form.save()
            messages.success(request, f'Orden de Trabajo #{orden_actualizada.id} actualizada correctamente (Estado: {orden_actualizada.estado}).')
            return redirect('ordenes_listar')
    else:
        form = OrdenTrabajoForm(instance=orden)
    return render(request, 'mantenimiento/orden_form.html', {
        'form': form, 
        'titulo': f'Modificar Orden de Trabajo #{orden.id}'
    })

# ELIMINAR ÓRDEN - Requiere permiso "Can delete Orden de Trabajo"
@permission_required('mantenimiento.delete_ordentrabajo', login_url='ordenes_listar', raise_exception=False)
def orden_eliminar(request, id):
    orden = get_object_or_404(OrdenTrabajo, id=id)
    if request.method == 'POST':
        orden.delete()
        messages.success(request, f'Orden #{id} eliminada correctamente.')
        return redirect('ordenes_listar')
    return render(request, 'mantenimiento/orden_confirmar_eliminar.html', {
        'orden': orden
    })