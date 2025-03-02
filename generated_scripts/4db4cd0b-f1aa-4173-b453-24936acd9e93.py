Here is a complete and executable Manim Python code for a bouncing ball animation:
```python
from manim import *

class BouncingBall(Scene):
    def construct(self):
        # Create a circle (ball) and move it to the top of the screen
        ball = Circle(radius=0.5, fill_opacity=1, color=BLUE)
        ball.move_to(UP * 3)
        self.add(ball)

        # Define the animation
        def update_ball(mob, alpha):
            x = 3 * np.sin(alpha)
            y = 3 * np.cos(alpha) - 9.8 * alpha**2
            mob.set_x(x)
            mob.set_y(y)
            return mob

        # Animate the ball bouncing
        self.play(UpdateFromAlphaFunc(ball, update_ball), run_time=5)

        # Wait for a second before ending the animation
        self.wait(1)
```
This code creates a blue circle (the ball) and moves it to the top of the screen. Then, it defines an `update_ball` function that updates the ball's position based on the animation time `alpha`. The ball's x-coordinate oscillates sinusoidally, while its y-coordinate follows a parabolic path, simulating gravity. Finally, the code animates the ball bouncing using `UpdateFromAlphaFunc` and waits for a second before ending the animation.

To run this code, save it to a file (e.g., `bouncing_ball.py`) and execute it with Manim using `manim -p -c WHITE bouncing_ball.py BouncingBall`.