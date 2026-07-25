from CRUD.controlador_servicios import ControladorServicios
from exceptions.excepciones import CostoInvalidoError, ServicioNoEncontradoError


class RepositorioEjemplo:
    def crear(self, servicio):
        return 1

    def eliminar(self, servicio_id):
        raise ServicioNoEncontradoError(servicio_id)


controlador = ControladorServicios(RepositorioEjemplo())

try:
    controlador.registrar("Luis", "Toyota", "Frenos", -200)
except CostoInvalidoError as error:
    print("Caso 1:", error)

try:
    controlador.eliminar(999)
except ServicioNoEncontradoError as error:
    print("Caso 2:", error)

