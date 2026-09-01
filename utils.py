def filtrar_por_texto(datos: list[dict], query:str, campos: list[str]) -> list[dict]:
    """
    Filtra una lista de diccionarios según un texto de búsqueda en campos específicos.

    Args:
        datos (list[dict]): Lista de diccionarios a filtrar.
        query (str): Texto de búsqueda.
        campos (list[str]): Lista de campos en los que buscar el texto.

    Returns:
        list[dict]: Lista filtrada de diccionarios que contienen el texto de búsqueda en los campos especificados.
    """
    if not query:
        return datos

    termino = query.strip().lower()
    resultados = []

    for item in datos:
        coincide = any(
            termino in str(item.get(campo, '')).lower() for campo in campos
        )
        if coincide:
            resultados.append(item)

    return resultados