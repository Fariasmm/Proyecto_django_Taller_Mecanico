import json
from pathlib import Path
from django.shortcuts import render
from utils import filtrar_por_texto

BASE_DIR = Path(__file__).resolve().parent.parent

def catalogo_repuestos(request):
    ruta_json = BASE_DIR / 'repuestos' / 'data' / 'repuestos.json'

    with open(ruta_json, 'r', encoding='utf-8') as archivo:
        repuestos_data = json.load(archivo)

    query = request.GET.get('q', '')

    repuestos_resultado = filtrar_por_texto(
        repuestos_data,
        query = query,
        campos=['nombre', 'descripcion']
    )

    return render(request, 'repuestos/catalogo.html',{
        'repuestos': repuestos_resultado,
        'total_items': len(repuestos_resultado),
        'busqueda': query
    })

def cotizador_repuestos(request):
    ruta_json = BASE_DIR / 'repuestos' / 'data' / 'repuestos.json'

    with open(ruta_json, 'r', encoding='utf-8') as archivo:
        repuestos_data = json.load(archivo)

    precios = [item['precio'] for item in repuestos_data]
    promedio = sum(precios) / len(precios) if precios else 0

    return render(request, 'repuestos/cotizador.html', {
        'repuestos': repuestos_data,
        'precio_promedio': int(promedio)
    })