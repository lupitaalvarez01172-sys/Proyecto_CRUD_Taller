import pytest

from CRUD.servicio import Servicio
from exceptions.excepciones import CostoInvalidoError


def test_servicio_valido():
    # Arrange
    servicio = Servicio(None, "María", "Nissan", "Afinación", 1200)

    # Act
    resultado = servicio.validar()

    # Assert
    assert resultado is None


def test_costo_debe_ser_mayor_a_cero():
    # Arrange
    servicio = Servicio(None, "María", "Nissan", "Afinación", -10)

    # Act y Assert
    with pytest.raises(CostoInvalidoError):
        servicio.validar()


def test_cliente_es_obligatorio():
    # Arrange
    servicio = Servicio(None, "", "Nissan", "Afinación", 500)

    # Act y Assert
    with pytest.raises(ValueError, match="cliente"):
        servicio.validar()

