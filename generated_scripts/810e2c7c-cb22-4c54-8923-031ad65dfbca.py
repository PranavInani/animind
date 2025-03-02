from manim import *

class BouncingBall(Scene):
    def construct(self):
        # Create a circle to represent the ball
        ball = Circle(radius=0.5, color=BLUE, fill_opacity=1)

        # Add the ball to the scene
        self.add(ball)

        # Define the animation
        self.play(
            ball.animate.shift(UP * 2),
            rate_func=linear,
            run_time=1
        )

        # Bounce the ball
        for _ in range(5):
            self.play(
                ball.animate.shift(DOWN * 4),
                rate_func=there_and_back,
                run_time=2
            )
            self.wait(0.5)

        # Remove the ball from the scene
        self.remove(ball)

        # Hold the final frame for 2 seconds
        self.wait(2)