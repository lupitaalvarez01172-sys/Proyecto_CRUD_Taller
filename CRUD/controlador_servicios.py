from CRUD.servicio import Servicio


class ControladorServicios:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def registrar(self, cliente, vehiculo, tipo_servicio, costo):
        servicio = Servicio(None, cliente, vehiculo, tipo_servicio, float(costo))
        servicio.validar()
        return self.repositorio.crear(servicio)

    def consultar_todos(self):
        return self.repositorio.listar()

    def buscar(self, servicio_id):
        return self.repositorio.buscar_por_id(int(servicio_id))

    def actualizar(self, servicio_id, cliente, vehiculo, tipo_servicio, costo):
        servicio = Servicio(
            int(servicio_id), cliente, vehiculo, tipo_servicio, float(costo)
        )
        servicio.validar()
        self.repositorio.actualizar(servicio)

    def eliminar(self, servicio_id):
        self.repositorio.eliminar(int(servicio_id))

