
def formatear_nombre_completo(nombre_completo):
    # Divide el nombre completo en partes (nombres y apellidos)
    partes = nombre_completo.split()
    
    # Formatea cada parte para que la primera letra sea mayúscula y el resto minúscula
    partes_formateadas = [parte.capitalize() for parte in partes]
    
    # Une las partes formateadas con un espacio en blanco
    nombre_formateado = ' '.join(partes_formateadas)
    
    return nombre_formateado