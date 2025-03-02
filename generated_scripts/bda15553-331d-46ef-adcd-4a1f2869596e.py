from manim import *

class CircleToSquare(Animation):
    def __init__(self, circle, square, **kwargs):
        super().__init__(circle, **kwargs)
        self.square = square

    def create_animation(self):
        circle = self.mobject
        square = self.square
        self.rate_func = rush_from

        self.append_points(
            [
                circle.point_from_proportion(i / 4)
                for i in range(5)
            ]
        )
        self.append_points(
            [
                square.point_from_proportion(i / 4)
                for i in range(5)
            ]
        )

class CircleToSquareScene(Scene):
    def construct(self):
        circle = Circle(radius=2, color=BLUE)
        square = Square(side_length=4, color=RED)

        self.play(Create(circle))
        self.wait()
        self.play(CircleToSquare(circle, square))
        self.wait()

        self.play(Uncreate(square))
        self.wait()

        self.play(Create(circle))
        self.wait()

        self.play(CircleToSquare(circle, square))
        self.wait()

        self.play(Uncreate(square))
        self.wait()

        self.play(Create(circle))
        self.wait()

        self.play(CircleToSquare(circle, square))
        self.wait()