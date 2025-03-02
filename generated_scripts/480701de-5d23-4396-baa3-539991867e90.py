import numpy as np
from manim import *

class BouncingBall(Scene):
    def construct(self):
        # Create a circle to represent the ball
        ball = Circle(radius=0.5, color=WHITE).set_fill(WHITE)
        
        # Set the initial position of the ball at the top of the screen
        ball.shift(3 * UP)
        
        # Create a set to keep track of the ball's velocity
        velocity = np.array([0, 0])
        
        # Initialize the direction of the ball's movement
        velocity[1] = -2
        
        # Animation variables
        time = 0
        dt = 0.02
        
        # The animation loop
        def update_ball(mob):
            global time, velocity
            nonlocal dt
            
            # Apply gravity
            velocity[1] += -2 * dt
            
            # Update the ball's position
            ball.shift(dt * velocity)
            
            # Collision detection
            if ball.get_bottom()[1] < -4 or ball.get_top()[1] > 4:
                # Reverse the vertical component of the velocity
                velocity[1] = -velocity[1]
            
            time += dt
            
        self.add(ball)
        self.play(UpdateFromFunc(ball, update_ball), run_time=5, rate_func=linear)
        self.wait(1)