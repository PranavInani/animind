from manim import *

class DefaultScene(Scene):
    def construct(self):
        # Example animation: A simple square that rotates
        square = Square()
        self.play(Create(square))
        self.play(square.animate.rotate(PI / 4))
        self.play(FadeOut(square))