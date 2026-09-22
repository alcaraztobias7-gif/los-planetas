from tkinter import *
import random

puntaje = 0
numero_pregunta = 1
correcta = ""

# Lista para guardar los números de preguntas que ya salieron
preguntas_usadas = []

def siguiente_pregunta():
    global correcta

    # Generamos un número aleatorio que no esté en la lista
    numero = random.randint(1, 10)
    while numero in preguntas_usadas:
        numero = random.randint(1, 10)

    # Agregamos el número elegido a la lista de usadas
    preguntas_usadas.append(numero)

    # Estructura IF original
    if numero == 1:
        pregunta.config(text="¿Cual es el planeta mas grande del sistema solar?")
        correcta = "Jupiter"

    elif numero ==2:
        pregunta.config(text="¿Que planeta es conocido por sus grandes anillos?")
        correcta = "Saturno"
    elif numero == 3:
        pregunta.config(text="¿Cual es el planeta mas alejado del sol?")
        correcta = "Neptuno"

    elif numero == 4:
        pregunta.config(text="¿Cual es el planeta que tiene la gran mancha roja?")
        correcta = "Jupiter"

    elif numero == 5:
        pregunta.config(text="¿Cual de estos planetas es azul?")
        correcta = "Neptuno"

    elif numero == 6:
        pregunta.config(text="¿Que planeta gira casi de costado?")
        correcta = "Urano"

    elif numero ==7:
        pregunta.config(text="¿Que planeta tiene una gran cantidad de lunas?")
        correcta = "Jupiter"

    elif numero ==8:
        pregunta.config(text="¿Que planeta esta despues de saturno?")
        correcta = "Urano"

    elif numero ==9:
        pregunta.config(text="¿Que planeta esta despues de urano ?")
        correcta = "Neptuno"

    elif numero ==10:
        pregunta.config(text="¿Cual es el segundo planeta mas grande?")
        correcta = "Saturno"

# =====================
# VERIFICAR RESPUESTA
# =====================

def comprobar(boton):
    global puntaje, numero_pregunta

    respuesta = boton.cget("text")
    if respuesta == correcta:
        resultado.config(text="CORRECTO", fg="green")
        puntaje += 1
    else:
        resultado.config(text="INCORRECTO", fg="red")

    if numero_pregunta < 10:
        numero_pregunta += 1
        contador.config(text=f"Pregunta {numero_pregunta} de 10")
        siguiente_pregunta()
    else:
        pregunta.config(text="Juego Terminado")
        contador.config(text=f"Puntaje: {puntaje} de 10")
        for b in botones:
            b.config(state=DISABLED)

# =====================
# VENTANA PRINCIPAL
# =====================

base = Tk()
base.title("Trivia")
base.geometry("700x700")

# =====================
# FRAME SUPERIOR (PREGUNTAS)
# =====================

frame_superior = Frame(base, bg="lightblue")
frame_superior.pack(fill="both", expand=True)

titulo = Label(frame_superior, text="Trivia", font=("Arial", 20, "bold"), bg="lightyellow")
titulo.pack(pady=10)

contador = Label(frame_superior, text="Pregunta 1 de 10", font=("Arial", 14), bg="lightyellow")
contador.pack()

pregunta = Label(frame_superior, text="", font=("Arial", 16), wraplength=600, bg="lightyellow")
pregunta.pack(pady=15)

resultado = Label(frame_superior, text="", font=("Arial", 16, "bold"), bg="lightyellow")
resultado.pack(pady=5)

# =====================
# FRAME INFERIOR (BOTONES)
# =====================

frame_inferior = Frame(base, bg="lightyellow")
frame_inferior.pack(fill="both", expand=True, ipadx=10, ipady=10)

respuestas = ["Jupiter","Urano","Neptuno","Saturno",]

botones = []

for texto in respuestas:
    btn = Button(frame_inferior, text=texto, width=25, font=("Arial", 11), bg="white")
    btn.config(command=lambda b=btn: comprobar(b))
    btn.pack(pady=2)
    botones.append(btn)

# =====================
# INICIAR
# =====================

siguiente_pregunta()
base.mainloop()