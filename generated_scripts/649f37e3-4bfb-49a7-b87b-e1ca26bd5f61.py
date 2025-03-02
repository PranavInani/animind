from manim import *

class CircleToSquare(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=BLUE)

        self.play(Create(circle))
        self.wait(1)
        self.play(Transform(circle, square))
        self.wait(1)
        self.play(Transform(circle, Circle(color=BLUE)))
        self.wait(1)