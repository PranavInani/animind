from manim import *

class BouncingBall(Scene):
    def construct(self):
        # Create a circle for the ball
        ball = Circle(color=RED, radius=0.5)

        # Add the ball to the scene
        self.add(ball)

        # Set the initial position of the ball
        ball.shift(UP * 2)

        # Set the initial velocity of the ball
        velocity = DOWN * 2

        # Animate the ball bouncing
        self.play(
            ball.animate.shift(velocity),
            rate_func=linear,
            run_time=1
        )

        # Check for collision with the ground
        if ball.get_center()[1] < -3.5:
            # Reverse the velocity if collision occurs
            velocity = UP * 2

        # Animate the ball bouncing back up
        self.play(
            ball.animate.shift(velocity),
            rate_func=linear,
            run_time=1
        )

        # Repeat the bouncing animation
        for _ in range(5):
            # Animate the ball moving down
            self.play(
                ball.animate.shift(DOWN * 2),
                rate_func=linear,
                run_time=1
            )

            # Animate the ball moving back up
            self.play(
                ball.animate.shift(UP * 2),
                rate_func=linear,
                run_time=1
            )

        # Remove the ball from the scene
        self.remove(ball)