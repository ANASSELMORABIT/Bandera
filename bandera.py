import turtle
import random
import time
wn = turtle.Screen()
banderra=turtle.Turtle()
def germany():
    banderra.reset()
    banderra.speed(1)
    banderra.fillcolor("black")
    banderra.begin_fill()
    for i in range(2):
        banderra.fd(150)
        banderra.rt(90)
        banderra.fd(30)
        banderra.rt(90)
    banderra.end_fill()

    banderra.pu()
    banderra.goto(0,-30)
    banderra.pd()

    banderra.fillcolor("red")
    banderra.begin_fill()
    for i in range(2):
        banderra.fd(150)
        banderra.rt(90)
        banderra.fd(30)
        banderra.rt(90)
    banderra.end_fill()

    banderra.pu()
    banderra.goto(0,-60)
    banderra.pd()
    banderra.fillcolor("yellow")
    banderra.begin_fill()
    for i in range(2):
        banderra.fd(150)
        banderra.rt(90)
        banderra.fd(30)
        banderra.rt(90)
    banderra.end_fill()
    time.sleep(2)
def italy():
    banderra.reset()
    banderra.speed(1)
    banderra.fillcolor("green")
    banderra.begin_fill()
    for i in range(2):
        banderra.fd(80)
        banderra.rt(90)
        banderra.fd(150)
        banderra.rt(90)
    banderra.end_fill()

    banderra.pu()
    banderra.goto(80,0)
    banderra.pd()

    banderra.fillcolor("white")
    banderra.begin_fill()
    for i in range(2):
        banderra.fd(80)
        banderra.rt(90)
        banderra.fd(150)
        banderra.rt(90)
    banderra.end_fill()

    banderra.pu()
    banderra.goto(160,0)
    banderra.pd()
    banderra.fillcolor("red")
    banderra.begin_fill()
    for i in range(2):
        banderra.fd(80)
        banderra.rt(90)
        banderra.fd(150)
        banderra.rt(90)
    banderra.end_fill()
    time.sleep(2)
def france():
    banderra.reset()
    banderra.speed(1)
    banderra.fillcolor("blue")
    banderra.begin_fill()
    for i in range(2):
        banderra.fd(80)
        banderra.rt(90)
        banderra.fd(150)
        banderra.rt(90)
    banderra.end_fill()

    banderra.pu()
    banderra.goto(80,0)
    banderra.pd()

    banderra.fillcolor("white")
    banderra.begin_fill()
    for i in range(2):
        banderra.fd(80)
        banderra.rt(90)
        banderra.fd(150)
        banderra.rt(90)
    banderra.end_fill()

    banderra.pu()
    banderra.goto(160,0)
    banderra.pd()
    banderra.fillcolor("red")
    banderra.begin_fill()
    for i in range(2):
        banderra.fd(80)
        banderra.rt(90)
        banderra.fd(150)
        banderra.rt(90)
    banderra.end_fill()
    time.sleep(2)
def Hollanda():
    banderra.reset()
    banderra.speed(1)
    banderra.fillcolor("red")
    banderra.begin_fill()
    for i in range(2):
        banderra.fd(150)
        banderra.rt(90)
        banderra.fd(30)
        banderra.rt(90)
    banderra.end_fill()

    banderra.pu()
    banderra.goto(0,-30)
    banderra.pd()

    banderra.fillcolor("white")
    banderra.begin_fill()
    for i in range(2):
        banderra.fd(150)
        banderra.rt(90)
        banderra.fd(30)
        banderra.rt(90)
    banderra.end_fill()

    banderra.pu()
    banderra.goto(0,-60)
    banderra.pd()
    banderra.fillcolor("blue")
    banderra.begin_fill()
    for i in range(2):
        banderra.fd(150)
        banderra.rt(90)
        banderra.fd(30)
        banderra.rt(90)
    banderra.end_fill()
    time.sleep(2)
def mostrar_mensaje(A):
    banderra.reset()
    banderra.speed(1)
    banderra.penup() 
    banderra.goto(0, 30)
    banderra.pendown() 
    banderra.write(A, align="center", font=("Arial", 24, "normal")) 
    time.sleep(1)
def juego():
    flag = [germany, italy, france, Hollanda]
    count=3
    while count>0:
        banderra_eligida = random.choice(flag)
        banderra_eligida()
        respuesta=input("¿A qué país pertenece esta bandera? (Escribe el nombre del país): ")
        if respuesta.lower()=="alemania" and banderra_eligida==germany:
            mostrar_mensaje("¡Correcto! Es la bandera de Alemania.")
            count=count+1
        elif respuesta.lower()=="italia" and banderra_eligida==italy:
            mostrar_mensaje("¡Correcto! Es la bandera de italia.")
            count=count+1
        elif respuesta.lower()=="francia" and banderra_eligida==france:
            mostrar_mensaje("¡Correcto! Es la bandera de francia.")
            count=count+1
        elif respuesta.lower()=="holanda" and banderra_eligida==Hollanda:
            mostrar_mensaje("¡Correcto! Es la bandera de holanda.")
            count=count+1
        else:
            mostrar_mensaje("Respuesta incorrecta. Inténtalo de nuevo.")
            count=count-1
        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ")
        if jugar_de_nuevo.lower() =="s" and count==0:
            mostrar_mensaje("Nos diculpamos,ha consumido la cantidad permitida de errores.")
            break
        if jugar_de_nuevo.lower() != "s":
            break
juego()
wn.exitonclick()

 