import json
from pathlib import Path
from django.shortcuts import render
from utils import filtrar_por_texto

BASE_DIR = Path(__file__).resolve().parent.parent

def inicio_mantenimiento(request):
    return render(request, 'mantenimiento/inicioM.html',{
        'titulo': 'Centro de Serivicos Mecanicos'
    })

def lista_servicios(request):
    ruta_json = BASE_DIR / 'mantenimiento'/ 'data' / 'servicios.json'

    with open(ruta_json, 'r', encoding='utf-8') as archivo:
        servicios_data = json.load(archivo)

    query = request.GET.get('q', '')

    servicios_resultado = filtrar_por_texto(
        datos= servicios_data,
        query=query,
        campos=['servicio', 'descripcion', 'nivel_prioridad']
    )

    return render(request, 'mantenimiento/servicios.html', {
        'servicios': servicios_resultado,
        'total_servicios': len(servicios_resultado),
        'busqueda': query
    })