from manim import *

class EquacaoQuadratica(Scene):
    def construct(self):
        # Título inicial
        titulo = Text("Raízes da Equação Quadrática", font_size=40, color=BLUE)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        # Forma geral
        eq1 = MathTex("a", "x^2", "+", "b", "x", "+", "c", "=", "0", font_size=48)
        eq1.set_color_by_tex_to_color_map({
            "a": RED, "b": GREEN, "c": BLUE, "x": YELLOW
        })
        self.play(Write(eq1))
        self.wait(2)

        # Dividindo por a
        texto_div = Text("Dividindo por a", font_size=32, color=YELLOW).to_edge(UP)
        eq2 = MathTex("x^2", "+", "\\frac{b}{a}", "x", "+", "\\frac{c}{a}", "=", "0", font_size=48)
        eq2.set_color_by_tex_to_color_map({
            "b": GREEN, "a": RED, "c": BLUE, "x": YELLOW
        })
        self.play(Write(texto_div))
        self.play(Transform(eq1, eq2))
        self.wait(2)
        self.play(FadeOut(texto_div))

        # Isolando termo constante
        texto_mover = Text("Isolando o termo constante", font_size=32, color=ORANGE).to_edge(UP)
        eq3 = MathTex("x^2", "+", "\\frac{b}{a}", "x", "=", "-\\frac{c}{a}", font_size=48)
        eq3.set_color_by_tex_to_color_map({
            "b": GREEN, "a": RED, "c": BLUE, "x": YELLOW
        })
        self.play(Write(texto_mover))
        self.play(Transform(eq1, eq3))
        self.wait(2)
        self.play(FadeOut(texto_mover))

        # Completando quadrado
        texto_completa = Text("Completando o quadrado", font_size=32, color=GREEN).to_edge(UP)
        eq4 = MathTex(
            "x^2", "+", "\\frac{b}{a}", "x", "+", "\\left(\\frac{b}{2a}\\right)^2",
            "=", "-\\frac{c}{a}", "+", "\\left(\\frac{b}{2a}\\right)^2",
            font_size=38
        )
        eq4.set_color_by_tex_to_color_map({
            "b": GREEN, "a": RED, "c": BLUE, "x": YELLOW
        })
        self.play(Write(texto_completa))
        self.play(Transform(eq1, eq4))
        self.wait(3)
        self.play(FadeOut(texto_completa))

        # Quadrado perfeito
        texto_fatorado = Text("Quadrado perfeito formado", font_size=32, color=PURPLE).to_edge(UP)
        eq5 = MathTex(
            "\\left(x + \\frac{b}{2a}\\right)^2", "=", "\\frac{b^2 - 4ac}{4a^2}",
            font_size=42
        )
        eq5.set_color_by_tex_to_color_map({
            "b": GREEN, "a": RED, "c": BLUE, "x": YELLOW
        })
        self.play(Write(texto_fatorado))
        self.play(Transform(eq1, eq5))
        self.wait(3)
        self.play(FadeOut(texto_fatorado))

        # Extração da raiz
        texto_raiz = Text("Extraindo a raiz quadrada", font_size=32, color=TEAL).to_edge(UP)
        eq6 = MathTex(
            "x + \\frac{b}{2a}", "=", "\\pm \\frac{\\sqrt{b^2 - 4ac}}{2a}",
            font_size=44
        )
        eq6.set_color_by_tex_to_color_map({
            "b": GREEN, "a": RED, "c": BLUE, "x": YELLOW
        })
        self.play(Write(texto_raiz))
        self.play(Transform(eq1, eq6))
        self.wait(2)
        self.play(FadeOut(texto_raiz))

        # Isolando x
        texto_final = Text("Isolando o x", font_size=32, color=RED).to_edge(UP)
        eq_final = MathTex(
            "x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}",
            font_size=48,
            color=WHITE
        )
        eq_final.set_color_by_tex_to_color_map({
            "b": GREEN, "a": RED, "c": BLUE, "x": YELLOW
        })
        self.play(Write(texto_final))
        self.play(Transform(eq1, eq_final))
        self.wait(3)

        # Conclusão
        conclusao = Text("Formula de Bhaskara", font_size=32, color=BLUE).next_to(eq1, DOWN)
        self.play(Write(conclusao))
        self.wait(2)

        # Finalização
        self.play(FadeOut(texto_final), FadeOut(eq1), FadeOut(conclusao))
