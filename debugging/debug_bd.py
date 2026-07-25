import pdb

from CRUD.repositorio_servicios import RepositorioServicios


def buscar_servicio():
    repositorio = RepositorioServicios()
    servicio_id = 1
    pdb.set_trace()
    servicio = repositorio.buscar_por_id(servicio_id)
    print(servicio)


if __name__ == "__main__":
    buscar_servicio()

