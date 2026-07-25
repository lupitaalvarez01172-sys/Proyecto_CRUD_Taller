import pdb

from CRUD.servicio import Servicio


def revisar_servicio():
    servicio = Servicio(1, "María", "Nissan Versa", "Afinación", 1200)
    pdb.set_trace()
    servicio.validar()
    print("Servicio válido:", servicio)


if __name__ == "__main__":
    revisar_servicio()

