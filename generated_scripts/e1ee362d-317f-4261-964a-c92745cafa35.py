from manim import *

class BouncingBall(Scene):
    def construct(self):
        # Create a circle to represent the ball
        ball = Circle(radius=0.5, color=BLUE, fill_opacity=1)

        # Add the ball to the scene
        self.add(ball)

        # Define the initial position of the ball
        ball.shift(UP * 2)

        # Define the animation
        self.play(
            ball.animate.shift(DOWN * 4),
            rate_func=there_and_back,
            run_time=2
        )

        # Repeat the animation indefinitely
        self.wait(1)
        self.play(
            ball.animate.shift(DOWN * 4),
            rate_func=there_and_back,
            run_time=2
        )
        self.wait(1)

        # Keep the scene for 2 seconds before closing
        self.wait(2)