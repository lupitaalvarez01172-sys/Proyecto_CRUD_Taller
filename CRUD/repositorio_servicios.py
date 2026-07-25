import mysql.connector

from CRUD.servicio import Servicio
from exceptions.excepciones import ServicioDuplicadoError, ServicioNoEncontradoError


class RepositorioServicios:
    def __init__(self, host="localhost", user="root", password="", database="taller_mecanico"):
        self.configuracion = {
            "host": host,
            "user": user,
            "password": password,
            "database": database,
        }

    def _conectar(self):
        return mysql.connector.connect(**self.configuracion)

    def crear(self, servicio: Servicio) -> int:
        conexion = None
        cursor = None
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()
            cursor.execute(
                """SELECT id FROM servicios
                   WHERE cliente=%s AND vehiculo=%s AND tipo_servicio=%s""",
                (servicio.cliente, servicio.vehiculo, servicio.tipo_servicio),
            )
            if cursor.fetchone():
                raise ServicioDuplicadoError()

            cursor.execute(
                """INSERT INTO servicios(cliente, vehiculo, tipo_servicio, costo)
                   VALUES (%s, %s, %s, %s)""",
                (servicio.cliente, servicio.vehiculo, servicio.tipo_servicio, servicio.costo),
            )
            conexion.commit()
        except mysql.connector.Error:
            if conexion:
                conexion.rollback()
            raise
        else:
            return cursor.lastrowid
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    def listar(self) -> list[Servicio]:
        conexion = None
        cursor = None
        try:
            conexion = self._conectar()
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT id, cliente, vehiculo, tipo_servicio, costo FROM servicios ORDER BY id")
            return [Servicio(**fila) for fila in cursor.fetchall()]
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    def buscar_por_id(self, servicio_id: int) -> Servicio:
        conexion = None
        cursor = None
        try:
            conexion = self._conectar()
            cursor = conexion.cursor(dictionary=True)
            cursor.execute(
                "SELECT id, cliente, vehiculo, tipo_servicio, costo FROM servicios WHERE id=%s",
                (servicio_id,),
            )
            fila = cursor.fetchone()
            if not fila:
                raise ServicioNoEncontradoError(servicio_id)
            return Servicio(**fila)
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    def actualizar(self, servicio: Servicio) -> None:
        conexion = None
        cursor = None
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()
            cursor.execute(
                """UPDATE servicios SET cliente=%s, vehiculo=%s,
                   tipo_servicio=%s, costo=%s WHERE id=%s""",
                (
                    servicio.cliente,
                    servicio.vehiculo,
                    servicio.tipo_servicio,
                    servicio.costo,
                    servicio.id,
                ),
            )
            if cursor.rowcount == 0:
                raise ServicioNoEncontradoError(servicio.id)
            conexion.commit()
        except Exception:
            if conexion:
                conexion.rollback()
            raise
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

    def eliminar(self, servicio_id: int) -> None:
        conexion = None
        cursor = None
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM servicios WHERE id=%s", (servicio_id,))
            if cursor.rowcount == 0:
                raise ServicioNoEncontradoError(servicio_id)
            conexion.commit()
        except Exception:
            if conexion:
                conexion.rollback()
            raise
        finally:
            if cursor:
                cursor.close()
            if conexion and conexion.is_connected():
                conexion.close()

