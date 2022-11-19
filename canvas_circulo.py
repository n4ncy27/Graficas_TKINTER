from tkinter import *
import random

#--------------------------
# variables globales
#--------------------------

BASE = 460
ALTURA = 380

#--------------------------
# ventana principal
#--------------------------

ventana_principal = Tk()
ventana_principal.title("Graficas 2D  - Texto")
#ventana_principal.resizable(False,False)
ventana_principal.config(bg="green")


#--------------------------
# frame de graficación
#--------------------------

frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="white", width=480, height=400)
frame_graficacion.pack(fill=BOTH, padx=10, pady=10)

# creación canvas
c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.place(x=10,y=10)

# texto
#texto = c.create_text(BASE/2, ALTURA/2, anchor="center", text="UIS Socorro", font=("Arial", "30", "bold"),fill="blue", activefill="red")


#lineas
#lineal = c.create_line(0,0,BASE, ALTURA,fill="red")
#linea2 = c.create_line(0, ALTURA, BASE, 0, fill="red")
#linea3 = c.create_line(BASE/2, 0, BASE/2, ALTURA, fill="blue")
#linea4 = c.create_line(0, ALTURA/2, BASE,ALTURA/2, fill="blue")

x = 0
y = 0
for i in range(10):
    #R = random.randint(10,99)
    #G = random.randint(10,99)
    #B = random.randint(10,99)
    color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
    linea5 = c.create_line(0, ALTURA, BASE,x, fill=color)
    linea6 = c.create_line(BASE, ALTURA, 0,x, fill=color)
    linea6 = c.create_line(0, 0, y,BASE, fill=color)
    
    x = x + int(ALTURA/10)
    y = y + int(BASE/10)

#'#'+str(R)+str(G)+str(B)

# cuadrado y recctangulos 
#rect1 = c.create_rectangle(10,10,BASE/2-10,ALTURA/2-10,fill= "pink", outline="red")
#rect2 = c.create_rectangle(10,10,110,110,fill= "green")

# poligonos 
#poli1 = c.create_polygon(0,ALTURA, BASE/2,0, BASE, ALTURA, fill= "green", outline = "red", width=5)

poli1 = c.create_polygon(0,ALTURA/2, BASE/2,0, BASE, ALTURA/2,BASE/2, ALTURA, fill= "green", outline = "pink", width=5)






ventana_principal.mainloop()