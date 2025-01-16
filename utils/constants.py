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

class TipoMovimiento(PyEnum):
    INGRESO = "Ingreso"
    SALIDA = "Salida"


class TipoDocumento(PyEnum):
    FACTURA = "Factura"
    BOLETA_VENTA = "Boleta de Venta"
    TICKETS = "Ticket"
    MERCADO = "Mercado"
    LIQUIDACIÓN_DE_COMPRA = "Liquidación de compra"

class EstadoPago(PyEnum):
    PAGADO = "Pagado"
    PENDIENTE = "Pendiente"
    PARCIAL = "Parcial"

class DocumentoCliente(PyEnum):
    DNI = "DNI"
    RUC = "RUC"
    CE = "CE"

