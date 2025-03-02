from manim import *

class BouncingBall(Scene):
    def construct(self):
        # Create a circle to represent the ball
        ball = Circle(radius=0.5, color=RED, fill_opacity=1)

        # Set the initial position of the ball
        ball.shift(UP * 2)

        # Add the ball to the scene
        self.add(ball)

        # Set the animation to bounce the ball
        self.play(
            ball.animate.shift(DOWN * 4),
            rate_func=there_and_back,
            run_time=2
        )

        # Repeat the animation
        self.play(
            ball.animate.shift(DOWN * 4),
            rate_func=there_and_back,
            run_time=2
        )

        # Remove the ball from the scene
        self.remove(ball)

class BouncingBallRepeated(Animation):
    def __init__(self, ball, **kwargs):
        super().__init__(ball, **kwargs)
        self.ball = ball

    def create_animation(self):
        self.play(
            self.ball.animate.shift(DOWN * 4),
            rate_func=there_and_back,
            run_time=2
        )

class BouncingBallRepeatedScene(Scene):
    def construct(self):
        ball = Circle(radius=0.5, color=RED, fill_opacity=1)
        ball.shift(UP * 2)
        self.add(ball)

        animation = BouncingBallRepeated(ball)
        self.play(animation)
        self.wait()

        self.play(animation)
        self.wait()

        self.remove(ball)

# Run the scene
class BouncingBallRepeatedSceneFinal(Scene):
    def construct(self):
        ball = Circle(radius=0.5, color=RED, fill_opacity=1)
        ball.shift(UP * 2)
        self.add(ball)

        for _ in range(5):
            self.play(
                ball.animate.shift(DOWN * 4),
                rate_func=there_and_back,
                run_time=2
            )

        self.remove(ball)