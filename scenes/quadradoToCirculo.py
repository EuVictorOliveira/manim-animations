from manim import *

class Quadrado(Scene):
    def construct(self):

        quadrado = Square()
        quadrado.set_fill(PURPLE, opacity=0.5)
        quadrado.rotate(PI/4)

        circulo = Circle()
        circulo.set_fill(BLUE, opacity=0.5)

        self.play(Create(quadrado))
        self.play(Transform(quadrado, circulo))

        self.wait(1)


