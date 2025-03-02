from manim import *

class BouncingBall(Scene):
    def construct(self):
        # Create a circle to represent the ball
        ball = Circle(color=BLUE, fill_opacity=0.5).scale(0.5)

        # Add the ball to the scene
        self.add(ball)

        # Define the bouncing animation
        self.play(
            ball.animate.shift(UP * 2), 
            rate_func=there_and_back, 
            run_time=2
        )

        # Repeat the animation
        for _ in range(5):
            self.play(
                ball.animate.shift(DOWN * 2), 
                rate_func=there_and_back, 
                run_time=1.5
            )
            self.play(
                ball.animate.shift(UP * 2), 
                rate_func=there_and_back, 
                run_time=1.5
            )

        # Remove the ball from the scene
        self.remove(ball)