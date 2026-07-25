from dataclasses import dataclass

from exceptions.excepciones import CostoInvalidoError


@dataclass
class Servicio:
    id: int | None
    cliente: str
    vehiculo: str
    tipo_servicio: str
    costo: float

    def validar(self) -> None:
        if not self.cliente.strip():
            raise ValueError("El nombre del cliente es obligatorio")
        if not self.vehiculo.strip():
            raise ValueError("El vehículo es obligatorio")
        if not self.tipo_servicio.strip():
            raise ValueError("El tipo de servicio es obligatorio")
        if self.costo <= 0:
            raise CostoInvalidoError(self.costo)

