from manim import *

class TwinklingStar(Animation):
    def __init__(self, star, rate=0.1, **kwargs):
        self.star = star
        self.rate = rate
        super().__init__(self.star, **kwargs)

    def interpolate_mobject(self, alpha):
        self.star.set_stroke(opacity=0.5 + 0.5 * np.sin(alpha * np.pi * self.rate))

class StarTwinkling(Scene):
    def construct(self):
        star = Star(color=WHITE, stroke_width=2).scale(0.5).move_to(ORIGIN)
        self.add(star)
        self.play(TwinklingStar(star), run_time=5)