import pytest

from CRUD.controlador_servicios import ControladorServicios
from CRUD.servicio import Servicio
from exceptions.excepciones import ServicioDuplicadoError, ServicioNoEncontradoError


class RepositorioFalso:
    def __init__(self):
        self.servicios = []
        self.siguiente_id = 1

    def crear(self, servicio):
        duplicado = any(
            s.cliente == servicio.cliente
            and s.vehiculo == servicio.vehiculo
            and s.tipo_servicio == servicio.tipo_servicio
            for s in self.servicios
        )
        if duplicado:
            raise ServicioDuplicadoError()
        servicio.id = self.siguiente_id
        self.siguiente_id += 1
        self.servicios.append(servicio)
        return servicio.id

    def listar(self):
        return self.servicios

    def buscar_por_id(self, servicio_id):
        for servicio in self.servicios:
            if servicio.id == servicio_id:
                return servicio
        raise ServicioNoEncontradoError(servicio_id)

    def actualizar(self, servicio):
        for indice, actual in enumerate(self.servicios):
            if actual.id == servicio.id:
                self.servicios[indice] = servicio
                return
        raise ServicioNoEncontradoError(servicio.id)

    def eliminar(self, servicio_id):
        servicio = self.buscar_por_id(servicio_id)
        self.servicios.remove(servicio)


@pytest.fixture
def controlador():
    return ControladorServicios(RepositorioFalso())


def test_registrar_y_consultar_servicio(controlador):
    # Arrange
    cliente = "María"

    # Act
    servicio_id = controlador.registrar(cliente, "Nissan", "Afinación", 1200)
    servicios = controlador.consultar_todos()

    # Assert
    assert servicio_id == 1
    assert len(servicios) == 1
    assert servicios[0].cliente == cliente


def test_no_registra_servicios_duplicados(controlador):
    # Arrange
    datos = ("María", "Nissan", "Afinación", 1200)
    controlador.registrar(*datos)

    # Act y Assert
    with pytest.raises(ServicioDuplicadoError):
        controlador.registrar(*datos)


def test_actualizar_servicio(controlador):
    # Arrange
    servicio_id = controlador.registrar("María", "Nissan", "Afinación", 1200)

    # Act
    controlador.actualizar(servicio_id, "María", "Nissan", "Frenos", 1800)
    actualizado = controlador.buscar(servicio_id)

    # Assert
    assert actualizado.tipo_servicio == "Frenos"
    assert actualizado.costo == 1800


def test_eliminar_servicio(controlador):
    # Arrange
    servicio_id = controlador.registrar("María", "Nissan", "Afinación", 1200)

    # Act
    controlador.eliminar(servicio_id)

    # Assert
    with pytest.raises(ServicioNoEncontradoError):
        controlador.buscar(servicio_id)


def test_eliminar_servicio_inexistente(controlador):
    # Arrange
    servicio_id = 999

    # Act y Assert
    with pytest.raises(ServicioNoEncontradoError):
        controlador.eliminar(servicio_id)

