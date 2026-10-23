import math
import tkinter as tk
from tkinter import messagebox

class Notas:

    def __init__(self):
        self.lista_notas = [0.0] * 5

    def calcular_promedio(self):
        suma = sum(self.lista_notas)
        return suma / len(self.lista_notas)

    def calcular_desviacion(self):
        prom = self.calcular_promedio()
        suma = sum((nota - prom) ** 2 for nota in self.lista_notas)
        return math.sqrt(suma / len(self.lista_notas))

    def calcular_menor(self):
        return min(self.lista_notas)

    def calcular_mayor(self):
        return max(self.lista_notas)

class VentanaPrincipal(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Notas")
        self.geometry("280x380")
        self.resizable(False, False)
        self.update_idletasks()
        w, h = 280, 380
        x = (self.winfo_screenwidth() // 2) - (w // 2)
        y = (self.winfo_screenheight() // 2) - (h // 2)
        self.geometry(f"{w}x{h}+{x}+{y}")
        self.inicio()

    def inicio(self):
        self.txt_notas = []
        y_pos = 20

        for i in range(5):
            lbl = tk.Label(self, text=f"Nota {i+1}:", anchor="w")
            lbl.place(x=20, y=y_pos, width=80, height=23)
            txt = tk.Entry(self)
            txt.place(x=105, y=y_pos, width=135, height=23)
            self.txt_notas.append(txt)
            y_pos += 30

        self.calcular = tk.Button(
            self, text="Calcular", command=self.accion_calcular
        )
        self.calcular.place(x=20, y=170, width=100, height=23)

        self.limpiar = tk.Button(self, text="Limpiar", command=self.accion_limpiar)
        self.limpiar.place(x=125, y=170, width=80, height=23)

        self.promedio = tk.Label(self, text="Promedio = ", anchor="w")
        self.promedio.place(x=20, y=210, width=230, height=23)

        self.desviacion = tk.Label(self, text="Desviación estándar = ", anchor="w")
        self.desviacion.place(x=20, y=240, width=230, height=23)

        self.mayor = tk.Label(self, text="Nota mayor = ", anchor="w")
        self.mayor.place(x=20, y=270, width=230, height=23)

        self.menor = tk.Label(self, text="Nota menor = ", anchor="w")
        self.menor.place(x=20, y=300, width=230, height=23)

    def accion_calcular(self):
        try:
            for i, txt in enumerate(self.txt_notas):
                if not txt.get().strip():
                    raise ValueError(
                        f"Es obligatorio ingresar la nota {i+1}. No puede estar vacia."
                    )

            notas = Notas()
            for i in range(5):
                notas.lista_notas[i] = float(self.txt_notas[i].get())

            self.promedio.config(
                text=f"Promedio = {notas.calcular_promedio():.2f}"
            )
            self.desviacion.config(
                text=f"Desviacion estandar = {notas.calcular_desviacion():.2f}"
            )
            self.mayor.config(text=f"Valor mayor = {notas.calcular_mayor()}")
            self.menor.config(text=f"Valor menor = {notas.calcular_menor()}")

        except ValueError as ex:
            mensaje = (
                str(ex)
                if "obligatorio" in str(ex)
                else "Campo nulo o error en formato de numero"
            )
            messagebox.showerror("Error / Advertencia", mensaje)

    def accion_limpiar(self):
        for txt in self.txt_notas:
            txt.delete(0, tk.END)
        self.promedio.config(text="Promedio = ")
        self.desviacion.config(text="Desviacion estandar = ")
        self.mayor.config(text="Nota mayor = ")
        self.menor.config(text="Nota menor = ")

class Principal:

    @staticmethod
    def main():
        mi_ventana_principal = VentanaPrincipal()
        mi_ventana_principal.mainloop()


if __name__ == "__main__":
    Principal.main()