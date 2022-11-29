import pygame as pg
import pong
from pong import ANCHO, ALTO
from pong.pantallas import Menu, Partida

class Controlador:
    def __init__(self):
        pantalla_principal = pg.display.set_mode((ANCHO, ALTO))
        metronomo = pg.time.Clock()

        self.pantallas = [Menu(pantalla_principal, metronomo), Partida(pantalla_principal, metronomo)]

        self.menu = Menu(pantalla_principal, metronomo)
        self.partida = Partida(pantalla_principal, metronomo)

    def jugar(self):
        salida = False
        ix = 0
        while not salida:
        #while bool(salida) == False:
            salida = self.pantallas[ix].bucle_ppal()
            ix += 1
            if ix >= len(self.pantallas):
                ix = 0

            #ix = (ix + 1) % len(self.pantallas) 
            



