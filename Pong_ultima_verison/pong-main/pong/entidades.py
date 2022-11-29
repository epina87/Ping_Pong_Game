import pygame as pg


class Bola:
    def __init__(self, center_x, center_y, radio=10, color=(255, 255, 0)):
        self.center_x = center_x
        self.center_y = center_y
        self.color = color
        self.radio = radio

        self.vx = 0
        self.vy = 0

    def dibujar(self, pantalla):
        pg.draw.circle(pantalla, self.color, (self.center_x, self.center_y), self.radio)

    def mover(self, x_max = 800, y_max = 600):
        self.center_x += self.vx
        self.center_y += self.vy

        if self.center_y >= y_max - self.radio or self.center_y < self.radio:
            self.vy = self.vy * -1 

        if self.center_x >= x_max:
            self.center_x = x_max // 2
            self.center_y = y_max // 2

            self.vx *= -1
            self.vy *= -1

            return "LEFT"


        if self.center_x < 0:

            self.center_x = x_max // 2
            self.center_y = y_max // 2

            self.vx *= -1
            self.vy *= -1

            return "RIGHT"

    def comprobar_choque(self, *raquetas):
        for raqueta_activa in raquetas:
            if self.derecha >= raqueta_activa.izquierda and \
               self.izquierda <= raqueta_activa.derecha and \
               self.abajo >= raqueta_activa.arriba and \
               self.arriba <= raqueta_activa.abajo:

                self.vx *= -1
 

    @property
    def izquierda(self):
        return self.center_x - self.radio

    @property
    def derecha(self):
        return self.center_x + self.radio

    @property
    def arriba(self):
        return self.center_y - self.radio

    @property
    def abajo(self):
        return self.center_y + self.radio

class Raqueta:
    file_imagenes ={
        "drcha": ["electric00.png","electric01.png","electric02.png"],
        "izqda": ["electric00_.png","electric01_.png","electric02_.png"]
    }

    def __init__(self, center_x, center_y, w=120, h=20, color=(255, 255, 0)):
        self.center_x = center_x
        self.center_y = center_y
        self.color = color
        self.w = w
        self.h = h

        self.vx = 0
        self.vy = 0

        self.imagenes = self.__cargar_imagenes()
        self.direccion = 'izqda'
        self.imagen_activa = 0

        self.cambio_cada_x_fotogramas = 5
        self.cuenta_fotogramas = 0


        #self._imagen = pg.image.load(f"pong/images/{self.imagenes['izqda']}")  

    def __cargar_imagenes(self):
        imagenes = {}
        for lado in self.file_imagenes:
            imagenes[lado] = []
            for nombre_fichero in self.file_imagenes[lado]:
                foto = pg.image.load(f"pong/images/{nombre_fichero}")
                imagenes[lado].append(foto)

        return imagenes

    '''
    @property
    def imagen(self):
        return self._imagen

    @imagen.setter
    def imagen(self,valor):
        self._imagen = pg.image.load(f"pong/images/{self.imagenes[valor]}")
    '''
    
    def dibujar(self, pantalla):
        #pg.draw.rect(pantalla, self.color, (self.center_x - self.w // 2, self.center_y - self.h // 2, self.w, self.h))
        #pantalla.blit(self.imagen,(self.center_x - self.w // 2, self.center_y - self.h // 2))

        pantalla.blit(self.imagenes[self.direccion][self.imagen_activa],(self.center_x - self.w // 2, self.center_y - self.h // 2))
        self.cuenta_fotogramas += 1
        if self.cuenta_fotogramas == self.cambio_cada_x_fotogramas:

            self.imagen_activa += 1
            if self.imagen_activa>= len(self.imagenes[self.direccion]):
                self.imagen_activa =0
            self.cuenta_fotogramas =0 

    def mover(self, tecla_arriba, tecla_abajo, y_max=600):
        estado_teclas = pg.key.get_pressed()
        if estado_teclas[tecla_arriba]:
            self.center_y -= self.vy
        if self.center_y < self.h // 2:
            self.center_y = self.h // 2


        if estado_teclas[tecla_abajo]:
            self.center_y += self.vy
        if self.center_y > y_max - self.h // 2:
            self.center_y = y_max - self.h // 2

    @property
    def izquierda(self):
        return self.center_x - self.w // 2

    @property
    def derecha(self):
        return self.center_x + self.w // 2

    @property
    def arriba(self):
        return self.center_y - self.h // 2

    @property
    def abajo(self):
        return self.center_y + self.h // 2

