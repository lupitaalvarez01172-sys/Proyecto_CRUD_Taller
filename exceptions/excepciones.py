class ServicioNoEncontradoError(Exception):
    def __init__(self, servicio_id):
        super().__init__(f"No se encontró el servicio con ID {servicio_id}")


class CostoInvalidoError(Exception):
    def __init__(self, costo):
        super().__init__(f"El costo debe ser mayor a cero. Valor recibido: {costo}")


class ServicioDuplicadoError(Exception):
    def __init__(self):
        super().__init__("Ya existe un servicio igual para ese cliente y vehículo")

