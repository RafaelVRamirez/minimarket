from enum import Enum as PyEnum

class EstadoActivo(PyEnum):
    """
    Estado si esta Alta o Baja
    """
    ALTA = "Alta"
    BAJA = "Baja"

class EstadoProducto(PyEnum):
    ALTA = "Alta"
    BAJA = "Baja"
    AGOTADO = "Agotado"


class FormaPago(PyEnum):
    EFECTIVO = "Efectivo"
    TRANSFERENCIA = "Transferencia" # longitud 14
    YAPE = "Yape"
    CREDITO = "Crédito"

class CondicionPago(PyEnum):
    CONTADO = "Contado"
    CREDITO = "Crédito"


