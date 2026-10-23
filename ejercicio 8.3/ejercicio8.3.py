import math
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class FiguraGeometrica:

    def __init__(self):
        self.volumen = 0.0
        self.superficie = 0.0

    def set_volumen(self, volumen):
        self.volumen = volumen

    def set_superficie(self, superficie):
        self.superficie = superficie

    def get_volumen(self):
        return self.volumen

    def get_superficie(self):
        return self.superficie


class Cilindro(FiguraGeometrica):

    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        return math.pi * self.altura * (self.radio**2)

    def calcular_superficie(self):
        area_lado_a = 2.0 * math.pi * self.radio * self.altura
        area_lado_b = 2.0 * math.pi * (self.radio**2)
        return area_lado_a + area_lado_b


class Esfera(FiguraGeometrica):

    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        return (4.0 / 3.0) * math.pi * (self.radio**3)

    def calcular_superficie(self):
        return 4.0 * math.pi * (self.radio**2)


class Piramide(FiguraGeometrica):

    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        return ((self.base**2) * self.altura) / 3.0

    def calcular_superficie(self):
        area_base = self.base**2
        area_lado = 2.0 * self.base * self.apotema
        return area_base + area_lado

class Cubo(FiguraGeometrica):

    def __init__(self, lado):
        super().__init__()
        self.lado = lado
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        return self.lado**3

    def calcular_superficie(self):
        return 6.0 * (self.lado**2)

class Prisma(FiguraGeometrica):

    def __init__(self, base, altura, profundidad):
        super().__init__()
        self.base = base
        self.altura = altura
        self.profundidad = profundidad
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        return self.base * self.altura * self.profundidad

    def calcular_superficie(self):
        return 2.0 * (
            self.base * self.altura
            + self.base * self.profundidad
            + self.altura * self.profundidad
        )

class VentanaCilindro(tk.Toplevel):

    def __init__(self):
        super().__init__()
        self.title("Cilindro")
        self.geometry("300x280")
        self.resizable(False, False)
        self.inicio()

    def inicio(self):
        try:
            imagen_pil = Image.open("cilindro.png")
            imagen_pil = imagen_pil.resize(
                (80, 80), Image.Resampling.LANCZOS
            )
            self.img = ImageTk.PhotoImage(imagen_pil)

            lbl_img = tk.Label(self, image=self.img)
            lbl_img.place(x=200, y=20, width=80, height=80)
        except Exception:
            pass

        lbl_radio = tk.Label(self, text="Radio (cm):", anchor="w")
        lbl_radio.place(x=20, y=20, width=120, height=23)
        self.campo_radio = tk.Entry(self)
        self.campo_radio.place(x=100, y=20, width=90, height=23)

        lbl_altura = tk.Label(self, text="Altura (cm):", anchor="w")
        lbl_altura.place(x=20, y=50, width=120, height=23)
        self.campo_altura = tk.Entry(self)
        self.campo_altura.place(x=100, y=50, width=90, height=23)

        btn_calcular = tk.Button(
            self, text="Calcular", command=self.accion_calcular
        )
        btn_calcular.place(x=100, y=85, width=90, height=25)

        self.lbl_volumen = tk.Label(self, text="Volumen (cm3):", anchor="w")
        self.lbl_volumen.place(x=20, y=140, width=260, height=23)

        self.lbl_superficie = tk.Label(self, text="Superficie (cm2):", anchor="w")
        self.lbl_superficie.place(x=20, y=180, width=260, height=23)

    def accion_calcular(self):
        try:
            radio = float(self.campo_radio.get())
            altura = float(self.campo_altura.get())
            cilindro = Cilindro(radio, altura)
            self.lbl_volumen.config(
                text=f"Volumen (cm3): {cilindro.get_volumen():.2f}"
            )
            self.lbl_superficie.config(
                text=f"Superficie (cm2): {cilindro.get_superficie():.2f}"
            )
        except ValueError:
            messagebox.showerror(
                "Error", "Campo nulo o error en formato de numero"
            )


class VentanaEsfera(tk.Toplevel):

    def __init__(self):
        super().__init__()
        self.title("Esfera")
        self.geometry("300x260")
        self.resizable(False, False)
        self.inicio()

    def inicio(self):
        try:
            imagen_pil = Image.open("esfera.png")
            imagen_pil = imagen_pil.resize(
                (80, 80), Image.Resampling.LANCZOS
            )
            self.img = ImageTk.PhotoImage(imagen_pil)

            lbl_img = tk.Label(self, image=self.img)
            lbl_img.place(x=200, y=20, width=80, height=80)
        except Exception:
            pass

        lbl_radio = tk.Label(self, text="Radio (cm):", anchor="w")
        lbl_radio.place(x=20, y=20, width=120, height=23)
        self.campo_radio = tk.Entry(self)
        self.campo_radio.place(x=100, y=20, width=90, height=23)

        btn_calcular = tk.Button(
            self, text="Calcular", command=self.accion_calcular
        )
        btn_calcular.place(x=100, y=55, width=90, height=25)

        self.lbl_volumen = tk.Label(self, text="Volumen (cm3):", anchor="w")
        self.lbl_volumen.place(x=20, y=120, width=260, height=23)

        self.lbl_superficie = tk.Label(self, text="Superficie (cm2):", anchor="w")
        self.lbl_superficie.place(x=20, y=160, width=260, height=23)

    def accion_calcular(self):
        try:
            radio = float(self.campo_radio.get())
            esfera = Esfera(radio)
            self.lbl_volumen.config(
                text=f"Volumen (cm3): {esfera.get_volumen():.2f}"
            )
            self.lbl_superficie.config(
                text=f"Superficie (cm2): {esfera.get_superficie():.2f}"
            )
        except ValueError:
            messagebox.showerror(
                "Error", "Campo nulo o error en formato de numero"
            )


class VentanaPiramide(tk.Toplevel):

    def __init__(self):
        super().__init__()
        self.title("Piramide")
        self.geometry("300x300")
        self.resizable(False, False)
        self.inicio()

    def inicio(self):
        try:
            imagen_pil = Image.open("piramide.png")
            imagen_pil = imagen_pil.resize(
                (80, 80), Image.Resampling.LANCZOS
            )
            self.img = ImageTk.PhotoImage(imagen_pil)

            lbl_img = tk.Label(self, image=self.img)
            lbl_img.place(x=200, y=20, width=80, height=80)
        except Exception:
            pass

        lbl_base = tk.Label(self, text="Base (cm):", anchor="w")
        lbl_base.place(x=20, y=20, width=120, height=23)
        self.campo_base = tk.Entry(self)
        self.campo_base.place(x=100, y=20, width=90, height=23)

        lbl_altura = tk.Label(self, text="Altura (cm):", anchor="w")
        lbl_altura.place(x=20, y=50, width=120, height=23)
        self.campo_altura = tk.Entry(self)
        self.campo_altura.place(x=100, y=50, width=90, height=23)

        lbl_apotema = tk.Label(self, text="Apotema (cm):", anchor="w")
        lbl_apotema.place(x=20, y=80, width=120, height=23)
        self.campo_apotema = tk.Entry(self)
        self.campo_apotema.place(x=100, y=80, width=90, height=23)

        btn_calcular = tk.Button(
            self, text="Calcular", command=self.accion_calcular
        )
        btn_calcular.place(x=100, y=115, width=90, height=25)

        self.lbl_volumen = tk.Label(self, text="Volumen (cm3):", anchor="w")
        self.lbl_volumen.place(x=20, y=170, width=260, height=23)

        self.lbl_superficie = tk.Label(self, text="Superficie (cm2):", anchor="w")
        self.lbl_superficie.place(x=20, y=210, width=260, height=23)

    def accion_calcular(self):
        try:
            base = float(self.campo_base.get())
            altura = float(self.campo_altura.get())
            apotema = float(self.campo_apotema.get())
            piramide = Piramide(base, altura, apotema)
            self.lbl_volumen.config(
                text=f"Volumen (cm3): {piramide.get_volumen():.2f}"
            )
            self.lbl_superficie.config(
                text=f"Superficie (cm2): {piramide.get_superficie():.2f}"
            )
        except ValueError:
            messagebox.showerror(
                "Error", "Campo nulo o error en formato de numero"
            )

class VentanaCubo(tk.Toplevel):

    def __init__(self):
        super().__init__()
        self.title("Cubo")
        self.geometry("300x260")
        self.resizable(False, False)
        self.inicio()

    def inicio(self):
        try:
            imagen_pil = Image.open("cubo.png")
            imagen_pil = imagen_pil.resize(
                (80, 80), Image.Resampling.LANCZOS
            )
            self.img = ImageTk.PhotoImage(imagen_pil)

            lbl_img = tk.Label(self, image=self.img)
            lbl_img.place(x=200, y=20, width=80, height=80)
        except Exception:
            pass

        lbl_lado = tk.Label(self, text="Lado (cm):", anchor="w")
        lbl_lado.place(x=20, y=20, width=120, height=23)
        self.campo_lado = tk.Entry(self)
        self.campo_lado.place(x=100, y=20, width=90, height=23)

        btn_calcular = tk.Button(
            self, text="Calcular", command=self.accion_calcular
        )
        btn_calcular.place(x=100, y=55, width=90, height=25)

        self.lbl_volumen = tk.Label(self, text="Volumen (cm3):", anchor="w")
        self.lbl_volumen.place(x=20, y=120, width=260, height=23)

        self.lbl_superficie = tk.Label(self, text="Superficie (cm2):", anchor="w")
        self.lbl_superficie.place(x=20, y=160, width=260, height=23)

    def accion_calcular(self):
        try:
            lado = float(self.campo_lado.get())
            cubo = Cubo(lado)
            self.lbl_volumen.config(
                text=f"Volumen (cm3): {cubo.get_volumen():.2f}"
            )
            self.lbl_superficie.config(
                text=f"Superficie (cm2): {cubo.get_superficie():.2f}"
            )
        except ValueError:
            messagebox.showerror(
                "Error", "Campo nulo o error en formato de numero"
            )

class VentanaPrisma(tk.Toplevel):

    def __init__(self):
        super().__init__()
        self.title("Prisma")
        self.geometry("300x300")
        self.resizable(False, False)
        self.inicio()

    def inicio(self):
        try:
            imagen_pil = Image.open("prisma.png")
            imagen_pil = imagen_pil.resize(
                (80, 80), Image.Resampling.LANCZOS
            )
            self.img = ImageTk.PhotoImage(imagen_pil)

            lbl_img = tk.Label(self, image=self.img)
            lbl_img.place(x=200, y=20, width=80, height=80)
        except Exception:
            pass

        lbl_base = tk.Label(self, text="Base (cm):", anchor="w")
        lbl_base.place(x=20, y=20, width=120, height=23)
        self.campo_base = tk.Entry(self)
        self.campo_base.place(x=100, y=20, width=90, height=23)

        lbl_altura = tk.Label(self, text="Altura (cm):", anchor="w")
        lbl_altura.place(x=20, y=50, width=120, height=23)
        self.campo_altura = tk.Entry(self)
        self.campo_altura.place(x=100, y=50, width=90, height=23)

        lbl_prof = tk.Label(self, text="Profundidad:", anchor="w")
        lbl_prof.place(x=20, y=80, width=120, height=23)
        self.campo_prof = tk.Entry(self)
        self.campo_prof.place(x=100, y=80, width=90, height=23)

        btn_calcular = tk.Button(
            self, text="Calcular", command=self.accion_calcular
        )
        btn_calcular.place(x=100, y=115, width=90, height=25)

        self.lbl_volumen = tk.Label(self, text="Volumen (cm3):", anchor="w")
        self.lbl_volumen.place(x=20, y=170, width=260, height=23)

        self.lbl_superficie = tk.Label(self, text="Superficie (cm2):", anchor="w")
        self.lbl_superficie.place(x=20, y=210, width=260, height=23)

    def accion_calcular(self):
        try:
            base = float(self.campo_base.get())
            altura = float(self.campo_altura.get())
            profundidad = float(self.campo_prof.get())
            prisma = Prisma(base, altura, profundidad)
            self.lbl_volumen.config(
                text=f"Volumen (cm3): {prisma.get_volumen():.2f}"
            )
            self.lbl_superficie.config(
                text=f"Superficie (cm2): {prisma.get_superficie():.2f}"
            )
        except ValueError:
            messagebox.showerror(
                "Error", "Campo nulo o error en formato de numero"
            )

class VentanaPrincipal(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Figuras Geometricas")
        self.geometry("450x140")
        self.resizable(False, False)
        self.inicio()

    def inicio(self):
        btn_cilindro = tk.Button(
            self, text="Cilindro", command=self.abrir_cilindro
        )
        btn_cilindro.place(x=20, y=50, width=70, height=30)

        btn_esfera = tk.Button(self, text="Esfera", command=self.abrir_esfera)
        btn_esfera.place(x=100, y=50, width=70, height=30)

        btn_piramide = tk.Button(
            self, text="Piramide", command=self.abrir_piramide
        )
        btn_piramide.place(x=180, y=50, width=75, height=30)

        btn_cubo = tk.Button(self, text="Cubo", command=self.abrir_cubo)
        btn_cubo.place(x=265, y=50, width=70, height=30)

        btn_prisma = tk.Button(self, text="Prisma", command=self.abrir_prisma)
        btn_prisma.place(x=345, y=50, width=80, height=30)

    def abrir_cilindro(self):
        VentanaCilindro()

    def abrir_esfera(self):
        VentanaEsfera()

    def abrir_piramide(self):
        VentanaPiramide()

    def abrir_cubo(self):
        VentanaCubo()

    def abrir_prisma(self):
        VentanaPrisma()

class Principal:

    @staticmethod
    def main():
        app = VentanaPrincipal()
        app.mainloop()


if __name__ == "__main__":
    Principal.main()