from manim import *

class BouncingBall(Scene):
    def construct(self):
        # Create a circle to represent the ball
        ball = Circle(radius=0.5, color=BLUE, fill_opacity=1)

        # Add the ball to the scene
        self.add(ball)

        # Set the initial position of the ball
        ball.shift(UP * 2)

        # Animate the ball bouncing
        self.play(
            ball.animate.shift(DOWN * 4), 
            rate_func=there_and_back, 
            run_time=2
        )

        # Repeat the animation
        for _ in range(3):
            self.play(
                ball.animate.shift(DOWN * 2), 
                rate_func=there_and_back, 
                run_time=1.5
            )

        # Fade out the ball
        self.play(FadeOut(ball), run_time=0.5)

        # Wait for a second before ending the animation
        self.wait(1)