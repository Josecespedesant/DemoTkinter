#Es importante verificar que python y pip estan en el PATH --- abrir CMD y escribir:
#
#python --version
#
#pip -V
#
#debería de decir la versión de python y de pip, si no salen entonces agregarlos al PATH
#Seguidamente instalar tkinter
#
#pip install tk
#

#Imports de librerias externas
from tkinter import *
import random


#Declaracion de variables globales o constantes

#Ancho de la pantalla
WINDOW_WIDTH = 600
#Alto de la pantalla
WINDOW_HEIGHT = 500
#Alto y ancho del "mario"
IMG_WIDTH_HEIGHT = 41
#Color de fondo de la pantalla
BACKCOLOR = 'black'
#Velocidad a la que va la bola
xspeed = yspeed = 3
    

#Clase de la ventana para iniciar partida
class StartWindow:
    def __init__(self):
        #Configuracion de la ventana
        self.main_window = Tk()
        self.main_window.title("Donkey Kong")
        self.main_window.geometry(str(WINDOW_WIDTH)+"x"+str(WINDOW_HEIGHT))
        self.main_window.resizable(False,False)
        #Canvas donde se pondrá el label con el nombre
        self.main_canvas = Canvas(self.main_window, width = WINDOW_WIDTH, height = WINDOW_HEIGHT, background = BACKCOLOR)
        self.main_canvas.pack()
        #Label que desaparece y aparece en distintos lados (Un ejemplo de animacion)
        self.label = Label(self.main_canvas, text = "Jose Antonio Cespedes Downing", font = ('Helvetica 17 bold'), bg=BACKCOLOR, fg="white")
        self.label.pack()
        #Boton para empezar partida
        self.btn = Button(self.main_window, text='Start', width=10, height=5, bd='10', command=self.start_game_window)
        self.btn.place(x=100, y=250)
        #Inicia el rebote del label (importante que esté antes del mainloop)
        self.bounce()
        #Inicia la pantalla
        self.main_window.mainloop()

    #funcion que hace desaparecer y reaparecer el texto en distintos lugares
    def bounce(self):
        X = random.randint(1, WINDOW_WIDTH)
        Y = random.randint(1, WINDOW_HEIGHT)
        self.label.place(x=X,y=Y)
        self.main_window.after(1000, self.bounce)

    #funcion que cierra la ventana actual y empieza el "Juego"
    def start_game_window(self):
        self.main_window.destroy()
        GameWindow()


#Clase de la ventana del "Juego"
class GameWindow:
    def __init__(self):
        #Definicion de una ventana
        self.game_window = Tk()
        self.game_window.title("Donkey Kong")
        self.game_window.geometry(str(WINDOW_WIDTH)+"x"+str(WINDOW_HEIGHT))
        self.game_window.resizable(False,False)

        #Definicion de un canvas para el fondo
        self.game_canvas = Canvas(self.game_window, width = WINDOW_WIDTH, height = WINDOW_HEIGHT, background = BACKCOLOR)
        self.game_canvas.pack()

        #Creacion de la imagen
        self.img = PhotoImage(file='mario.png')
        self.my_image = self.game_canvas.create_image(30,WINDOW_HEIGHT-100,anchor=NW,image = self.img)

        #Crear una línea diagonal
                #create_line(x0,y0,x1,y1)
        self.game_canvas.create_line(
            (WINDOW_WIDTH/2)-100,
            WINDOW_HEIGHT/2,
            WINDOW_WIDTH,
            (WINDOW_HEIGHT/2)-30,
            fill="red",
            width=10)

        #Crear una bola que bajará por la línea
        self.ball = self.game_canvas.create_oval(WINDOW_WIDTH-40,
                                       (WINDOW_HEIGHT/2)-60,
                                       WINDOW_WIDTH-10,(WINDOW_HEIGHT/2)-30, fill="green")

        
        #Enlazar los eventos del teclado con los del frame 
        self.game_window.bind("<Left>", self.left)
        self.game_window.bind("<Right>", self.right)
        self.game_window.bind("<Up>", self.up)
        self.game_window.bind("<Down>", self.down)

        #Incia a rebotar la bola
        self.move_ball()

        #Cada cierto tiempo destruye la bola y crea otra nueva desde la misma posición
        #cada entre 1 y 10 segundos
        self.create_ball_destroy_previous()
        
        #Iniciar la app
        self.game_window.mainloop()

    #funcion que crea una bola en el mismo lugar y destruye la anterior
    def create_ball_destroy_previous(self):
        segundos_despues = random.randint(1,10) * 1000
        self.game_canvas.delete(self.ball)
        self.ball = self.game_canvas.create_oval(WINDOW_WIDTH-40,
                                       (WINDOW_HEIGHT/2)-60,
                                       WINDOW_WIDTH-10,(WINDOW_HEIGHT/2)-30, fill="green")
        self.game_canvas.after(segundos_despues, self.create_ball_destroy_previous)
        
    #funcion que hace que la bola se mueva y rebote en los bordes
    def move_ball(self): 
        global xspeed, yspeed
        self.game_canvas.move(self.ball, xspeed, yspeed)
        (leftPos, topPos, rightPos, bottomPos) = self.game_canvas.coords(self.ball)
        if leftPos <= 0 or rightPos >= WINDOW_WIDTH:
            xspeed = -xspeed
        if topPos <= 0 or bottomPos >= WINDOW_HEIGHT:
            yspeed = -yspeed
        self.game_canvas.after(30, self.move_ball)
    
    #Funciones de movimiento de mario en un canvas
    def left(self, event):
        x = -10
        y = 0
        self.game_canvas.move(self.my_image, x, y)

    def right(self, event):
        x = 10
        y = 0
        self.game_canvas.move(self.my_image, x, y)

    def up(self, event):
        x = 0
        y = -10
        self.game_canvas.move(self.my_image, x, y)

    def down(self, event):
        x = 0
        y = 10
        self.game_canvas.move(self.my_image, x, y)

#Inicia la ventana de inicio        
aplicacion = StartWindow()
