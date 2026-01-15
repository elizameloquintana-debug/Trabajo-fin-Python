def calcular_retorno_diario(precio_actual, precio_anterior):
    """
    Calcula el retorno porcentual entre dos precios.
    """
    return ((precio_actual - precio_anterior) / precio_anterior) * 100


def categorizar_volatilidad(desviacion_estandar):
    """
    Clasifica la volatilidad según la desviación estándar.
    """
    if desviacion_estandar < 2:
        return "Baja"
    elif 2 <= desviacion_estandar <= 5:
        return "Media"
    else:
        return "Alta"

# --------------------------------------------------
# Archivo: finanzas_utils.py
# Descripción:
# Este módulo contiene funciones reutilizables para
# el análisis financiero, específicamente para el
# cálculo de retornos porcentuales y la categorización
# de la volatilidad de un activo financiero.
#
# Las funciones fueron verificadas utilizando valores
# conocidos, comparando los resultados con cálculos
# manuales, obteniendo los valores esperados.
# --------------------------------------------------


def calcular_retorno_diario(precio_actual, precio_anterior):
    """
    Calcula el retorno porcentual entre dos precios.

    Parámetros:
    precio_actual (float): precio más reciente del activo
    precio_anterior (float): precio anterior o inicial

    Retorna:
    float: retorno porcentual
    """
    return ((precio_actual - precio_anterior) / precio_anterior) * 100


def categorizar_volatilidad(desviacion_estandar):
    """
    Clasifica la volatilidad según la desviación estándar.

    Parámetros:
    desviacion_estandar (float): desviación estándar en porcentaje

    Retorna:
    str: nivel de volatilidad ('Baja', 'Media' o 'Alta')
    """
    if desviacion_estandar < 2:
        return "Baja"
    elif 2 <= desviacion_estandar <= 5:
        return "Media"
    else:
        return "Alta"
