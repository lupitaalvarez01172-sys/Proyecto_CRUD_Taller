import tkinter as tk
from tkinter import messagebox, ttk


class InterfazTkinter:
    def __init__(self, controlador):
        self.controlador = controlador
        self.ventana = tk.Tk()
        self.ventana.title("Taller mecánico - Servicios")
        self.ventana.geometry("820x540")
        self.ventana.configure(bg="#eef3f8")
        self._crear_interfaz()
        self.cargar_tabla()

    def _crear_interfaz(self):
        titulo = tk.Label(
            self.ventana,
            text="Control de servicios del taller",
            font=("Arial", 20, "bold"),
            bg="#eef3f8",
            fg="#16324f",
        )
        titulo.pack(pady=18)

        formulario = tk.Frame(self.ventana, bg="#ffffff", padx=18, pady=14)
        formulario.pack(fill="x", padx=24)
        campos = [
            ("ID", "id"),
            ("Cliente", "cliente"),
            ("Vehículo", "vehiculo"),
            ("Tipo de servicio", "tipo"),
            ("Costo", "costo"),
        ]
        self.entradas = {}
        for columna, (etiqueta, clave) in enumerate(campos):
            tk.Label(formulario, text=etiqueta, bg="#ffffff").grid(
                row=0, column=columna, padx=5, sticky="w"
            )
            entrada = tk.Entry(formulario, width=15)
            entrada.grid(row=1, column=columna, padx=5, pady=5)
            self.entradas[clave] = entrada

        botones = tk.Frame(self.ventana, bg="#eef3f8")
        botones.pack(pady=14)
        acciones = [
            ("Registrar", self.registrar, "#198754"),
            ("Buscar", self.buscar, "#0d6efd"),
            ("Actualizar", self.actualizar, "#fd7e14"),
            ("Eliminar", self.eliminar, "#dc3545"),
            ("Limpiar", self.limpiar, "#6c757d"),
        ]
        for texto, comando, color in acciones:
            tk.Button(
                botones,
                text=texto,
                command=comando,
                bg=color,
                fg="white",
                width=12,
                relief="flat",
            ).pack(side="left", padx=5)

        columnas = ("id", "cliente", "vehiculo", "tipo", "costo")
        self.tabla = ttk.Treeview(self.ventana, columns=columnas, show="headings")
        encabezados = ("ID", "Cliente", "Vehículo", "Servicio", "Costo")
        for columna, encabezado in zip(columnas, encabezados):
            self.tabla.heading(columna, text=encabezado)
            self.tabla.column(columna, width=140, anchor="center")
        self.tabla.pack(fill="both", expand=True, padx=24, pady=(0, 20))
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar_fila)

    def _datos(self):
        return (
            self.entradas["cliente"].get(),
            self.entradas["vehiculo"].get(),
            self.entradas["tipo"].get(),
            self.entradas["costo"].get(),
        )

    def registrar(self):
        try:
            nuevo_id = self.controlador.registrar(*self._datos())
        except (ValueError, Exception) as error:
            messagebox.showerror("Error", str(error))
        else:
            messagebox.showinfo("Correcto", f"Servicio registrado con ID {nuevo_id}")
            self.cargar_tabla()
            self.limpiar()

    def buscar(self):
        try:
            servicio = self.controlador.buscar(self.entradas["id"].get())
        except Exception as error:
            messagebox.showerror("Error", str(error))
        else:
            self._mostrar_servicio(servicio)

    def actualizar(self):
        try:
            self.controlador.actualizar(self.entradas["id"].get(), *self._datos())
        except Exception as error:
            messagebox.showerror("Error", str(error))
        else:
            messagebox.showinfo("Correcto", "Servicio actualizado")
            self.cargar_tabla()

    def eliminar(self):
        try:
            self.controlador.eliminar(self.entradas["id"].get())
        except Exception as error:
            messagebox.showerror("Error", str(error))
        else:
            messagebox.showinfo("Correcto", "Servicio eliminado")
            self.cargar_tabla()
            self.limpiar()

    def cargar_tabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        try:
            servicios = self.controlador.consultar_todos()
        except Exception as error:
            messagebox.showerror("Base de datos", str(error))
            return
        for servicio in servicios:
            self.tabla.insert(
                "", "end",
                values=(
                    servicio.id,
                    servicio.cliente,
                    servicio.vehiculo,
                    servicio.tipo_servicio,
                    f"${servicio.costo:.2f}",
                ),
            )

    def seleccionar_fila(self, _evento):
        seleccion = self.tabla.selection()
        if seleccion:
            valores = self.tabla.item(seleccion[0], "values")
            for clave, valor in zip(("id", "cliente", "vehiculo", "tipo", "costo"), valores):
                entrada = self.entradas[clave]
                entrada.delete(0, tk.END)
                entrada.insert(0, str(valor).replace("$", ""))

    def _mostrar_servicio(self, servicio):
        valores = (servicio.id, servicio.cliente, servicio.vehiculo,
                   servicio.tipo_servicio, servicio.costo)
        for clave, valor in zip(("id", "cliente", "vehiculo", "tipo", "costo"), valores):
            self.entradas[clave].delete(0, tk.END)
            self.entradas[clave].insert(0, valor)

    def limpiar(self):
        for entrada in self.entradas.values():
            entrada.delete(0, tk.END)

    def ejecutar(self):
        self.ventana.mainloop()

