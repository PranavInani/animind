from manim import *

class BouncingBall(Scene):
    def construct(self):
        # Create a red circle
        ball = Circle(color=RED, radius=0.5)

        # Add the ball to the scene
        self.add(ball)

        # Animate the ball bouncing
        self.play(
            ball.animate.shift(UP * 2),
            rate_func=there_and_back,
            run_time=2
        )

        # Repeat the animation
        for _ in range(5):
            self.play(
                ball.animate.shift(RIGHT * 2),
                rate_func=there_and_back,
                run_time=2
            )
            self.play(
                ball.animate.shift(LEFT * 2),
                rate_func=there_and_back,
                run_time=2
            )

        # Remove the ball from the scene
        self.remove(ball)

        # Wait for a moment before ending the scene
        self.wait(1)