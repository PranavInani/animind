from manim import *

class SineWaveAnimation(Scene):
    def construct(self):
        # Create a sine wave
        sine_wave = FunctionGraph(lambda x: np.sin(x), x_range=[-10, 10], color=BLUE)

        # Add the sine wave to the scene
        self.add(sine_wave)

        # Animate the sine wave
        self.play(Create(sine_wave), run_time=3)

        # Wait for 2 seconds
        self.wait(2)