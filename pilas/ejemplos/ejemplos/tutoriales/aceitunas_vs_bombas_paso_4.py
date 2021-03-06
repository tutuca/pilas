import pilas
from pilas.actores import Bomba


class BombaConMovimiento(Bomba):

    def __init__(self, x=0, y=0):
        Bomba.__init__(self, x, y)

        self.circulo = pilas.fisica.Circulo(x, y, 20, restitucion=1, friccion=0, amortiguacion=0)
        self.imitar(self.circulo)

        self._empujar()

    def _empujar(self):
        dx = 1
        dy = 1
        self.circulo.impulsar(dx * 10, dy * 10)


def cuando_colisionan(aceituna, bomba):
    bomba.explotar()

pilas.iniciar(gravedad=(0,0))

protagonista = pilas.actores.Aceituna()
protagonista.aprender(pilas.habilidades.SeguirAlMouse)
pilas.mundo.motor.ocultar_puntero_del_mouse()

bomba_1 = BombaConMovimiento()
bomba_2 = BombaConMovimiento(x=200, y=0)
bomba_3 = BombaConMovimiento(x=0, y=200)

lista_de_bombas = [bomba_1, bomba_2, bomba_3]

pilas.mundo.colisiones.agregar(protagonista, lista_de_bombas, cuando_colisionan)

pilas.ejecutar()
