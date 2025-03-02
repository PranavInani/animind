from manim import *

class CircleToSquareToCircle(Animation):
    def __init__(self, circle, square, **kwargs):
        super().__init__(circle, **kwargs)
        self.square = square

    def create_animation(self):
        self.add_animation(Transform(self.mobject, self.square))

class CircleToSquare(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()

        # Alternative way using custom animation
        # self.play(CircleToSquareToCircle(circle, square))

        self.wait()

class Test(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)
        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()

        circle_to_square = CircleToSquareToCircle(circle, square)
        self.add_animation(circle_to_square)

        self.wait()

class SquareToCircle(Scene):
    def construct(self):
        square = Square(color=RED)
        circle = Circle(color=BLUE)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(Transform(circle, square))
        self.wait()

class CircleToSquareAndBackToCircle(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()

class Main(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()

        circle_to_square = CircleToSquareToCircle(circle, square)
        self.add_animation(circle_to_square)

        self.wait()

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()

        circle_to_square = CircleToSquareToCircle(circle, square)
        self.add_animation(circle_to_square)

        self.wait()

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()

        circle_to_square = CircleToSquareToCircle(circle, square)
        self.add_animation(circle_to_square)

        self.wait()

class Main2(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()

class CircleToSquareAndBackToCircle2(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()

class SquareToCircle2(Scene):
    def construct(self):
        square = Square(color=RED)
        circle = Circle(color=BLUE)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(Transform(circle, square))
        self.wait()

class Main3(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()

        circle_to_square = CircleToSquareToCircle(circle, square)
        self.add_animation(circle_to_square)

        self.wait()

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()

        circle_to_square = CircleToSquareToCircle(circle, square)
        self.add_animation(circle_to_square)

        self.wait()

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()

        circle_to_square = CircleToSquareToCircle(circle, square)
        self.add_animation(circle_to_square)

        self.wait()

class CircleToSquareAnimation(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()

class SquareToCircleAnimation(Scene):
    def construct(self):
        square = Square(color=RED)
        circle = Circle(color=BLUE)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(Transform(circle, square))
        self.wait()

class Main4(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()

class CircleToSquareAndBackToCircle3(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()

class Main5(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()

class CircleToSquareAndBackToCircle4(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()

class CircleToSquareAndBackToCircle5(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()

class CircleToSquareAndBackToCircle6(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()

class Main6(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()

class CircleToSquareAndBackToCircle7(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()

class CircleToSquareAndBackToCircle8(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()

class CircleToSquareAndBackToCircle9(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()

class Main7(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()

class CircleToSquareAndBackToCircle10(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()

class Main8(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()

class CircleToSquareAndBackToCircle11(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()

class CircleToSquareAndBackToCircle12(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()

class CircleToSquareAndBackToCircle13(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()

class Main9(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()

class CircleToSquareAndBackToCircle14(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()

class CircleToSquareAndBackToCircle15(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()

class Main10(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()

class CircleToSquareAndBackToCircle16(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()

class CircleToSquareAndBackToCircle17(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()

class CircleToSquareAndBackToCircle18(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()

class Main11(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()

class CircleToSquareAndBackToCircle19(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()

class CircleToSquareAndBackToCircle20(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Transform(square, circle))
        self.wait()