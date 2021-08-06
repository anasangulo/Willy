# Importaciones
# Importar modulo para poder hacer la parte gráfica
from tkinter import *
# Importar modulo para manejar imagenes
from PIL import Image
from PIL import ImageTk
# importamos modulo Funciones
import funciones
import calculos


def main():
    # Creamos la funcion ventana inicial Que inicia nuestra aplicacion
    def ventanainicial():

        def limpiar():
            # Funcion para limpiar los cuadros de texto en la ventana inicial
            txthidrometro.delete(0, END)
            txttemperatura.delete(0, END)
            print("Se limpio")

        def calcular():
            # Funcion para calcular el API
            print("Se van a realizar los calculos")
            hidrometro = txthidrometro.get()
            temperatura = txttemperatura.get()
            resultado = calculos.calculo(hidrometro, temperatura)
            api60f = round((141.5 / (resultado / 999.016)) - 131.5, 1)
            lblapiresultado['text'] = api60f
            lbldensidad['text'] = round(resultado/999.016, 4)
            

        # Destruimos la pantalla Splash
        splash.destroy()
        # Creando la ventana API
        ventanaapi = Tk()
        # Asignamos titulo a ventana API
        ventanaapi.title("CALCULADORA API")
        ventanaapi.iconbitmap('iconoApi.ico')
        
        # Asignamos el alto y el ancho de nuestra pantalla API
        anchoapp = 300
        altoapp = 600

        # Obtenemos el ancho y el alto de la pantalla del computador
        anchopantalla = ventanaapi.winfo_screenwidth()
        altopantalla = ventanaapi.winfo_screenheight()
        # Obtenemos las coordenadas del centro de la pantalla
        x = (anchopantalla / 2) - (anchoapp / 2)
        y = (altopantalla / 2) - (altoapp / 2)

        # Centramos la ventana api en la pantalla del computador
        ventanaapi.geometry(f"{anchoapp}x{altoapp}+{int(x)}+{int(y)}")

        # Crear frames para la aplicacion
        # En el Frame 1 se va a colocar la imagen de la aplicacion y en el frame 2 los labels , cuadro de texto y botones

        frame1 = Frame(ventanaapi)
        frame1.pack(expand=True, fill=BOTH)
        frame2 = Frame(ventanaapi)
        frame2.pack(expand=True, fill=BOTH)

        # Colocar la imagen de la aplicacion API en la ventana api
        miimagen2 = Image.open("imgApi.png")
        miimagen3 = miimagen2.resize((300, 300))
        render = ImageTk.PhotoImage(miimagen3)
        lblimagen2 = Label(frame1, image=render)
        lblimagen2.image = render
        lblimagen2.pack()

        # Creamos los labels que van en la ventana api
        lblhidrometro = Label(frame2, text="Lectura de Hidrometro")
        lbltemperatura = Label(frame2, text="Lectura de Termometro")
        lblapi = Label(frame2, text="API @ 60 F")
        lblresultado = Label(frame2, text="Densidad Relativa ")
        lblapiresultado = Label(frame2, text="Resultado API @ 60 F")
        lbldensidad = Label(frame2, text="Densidad Relativa")
        lblblackdog = Label(frame2, text="Design by: \n Black Dog Solutions")

        # Creamos los cuadros de texto que van en la pantalla inicial
        txthidrometro = Entry(frame2)
        txttemperatura = Entry(frame2)

        # Creamos los Botones que van en la pantalla inicial
        btncalcular = Button(frame2, text="Calcular", command=calcular)
        btnlimpiar = Button(frame2, text="Limpiar", command=limpiar)

        # Mostramos los elementos en la ventana api
        lblhidrometro.grid(row=0, column=0, padx=10, pady=8)
        lbltemperatura.grid(row=1, column=0, padx=10, pady=8)
        txthidrometro.grid(row=0, column=2, padx=10, pady=8)
        txttemperatura.grid(row=1, column=2, padx=10, pady=8)
        btncalcular.grid(row=2, column=0, padx=10, pady=8)
        btnlimpiar.grid(row=2, column=2, padx=10, pady=8)
        lblapi.grid(row=3, column=0, padx=10, pady=8)
        lblresultado.grid(row=4, column=0, padx=10, pady=8)
        lblapiresultado.grid(row=3, column=2, padx=10, pady=8)
        lbldensidad.grid(row=4, column=2, padx=10, pady=8)
        lblblackdog.grid(row=5, column=2, padx=10, pady=8)

    # Creando la pantalla Splash
    splash = Tk()
    # Esconder la barra de titulo en la pantalla Splash
    splash.overrideredirect(True)
    # Asignamos el alto y el ancho de nuestra pantalla Splash
    anchoapp = altoapp = 600

    # Obtenemos el ancho y el alto de la pantalla del computador
    anchopantalla = splash.winfo_screenwidth()
    altopantalla = splash.winfo_screenheight()
    # Obtenemos las coordenadas del centro de la pantalla
    x = (anchopantalla / 2) - (anchoapp / 2)
    y = (altopantalla / 2) - (altoapp / 2)

    # Centramos la pantalla Splash en la pantalla del computador
    splash.geometry(f"{anchoapp}x{altoapp}+{int(x)}+{int(y)}")

    # Colocar la imagen de la aplicacion API en la pantalla splash
    miimagen = ImageTk.PhotoImage(Image.open("imgApi.png"))
    lblimagen = Label(image=miimagen)
    lblimagen.pack()
    # temporizador de la pantalla Splash
    splash.after(2000, ventanainicial)

    mainloop()
