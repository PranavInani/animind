from manim import *

class BouncingBall(Scene):
    def construct(self):
        # Create a circle to represent the ball
        ball = Circle(radius=0.5, color=BLUE, fill_opacity=1)

        # Add the ball to the scene
        self.add(ball)

        # Define the animation
        self.play(
            ball.animate.shift(UP * 2),  # move the ball up
            rate_func=there_and_back,  # bounce the ball
            run_time=2  # duration of the animation
        )

        # Repeat the animation
        self.play(
            ball.animate.shift(DOWN * 2),  # move the ball down
            rate_func=there_and_back,  # bounce the ball
            run_time=2  # duration of the animation
        )

        # Repeat the animation multiple times
        for _ in range(5):
            self.play(
                ball.animate.shift(UP * 2),  # move the ball up
                rate_func=there_and_back,  # bounce the ball
                run_time=2  # duration of the animation
            )
            self.play(
                ball.animate.shift(DOWN * 2),  # move the ball down
                rate_func=there_and_back,  # bounce the ball
                run_time=2  # duration of the animation
            )