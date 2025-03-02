from manim import *

class GrowingTree(Animation):
    def __init__(self, tree, rate=0.1):
        super().__init__()
        self.tree = tree
        self.rate = rate

    def interpolate_mobject(self, alpha):
        self.tree.scale(alpha)

class Tree(Mobject):
    def __init__(self):
        super().__init__()
        self.trunk = Rectangle(width=0.5, height=2, color=BROWN)
        self.leaves = Circle(radius=1, color=GREEN)
        self.add(self.trunk, self.leaves)
        self.trunk.shift(UP)
        self.leaves.shift(UP * 1.5)

class GrowingTreeScene(Scene):
    def construct(self):
        tree = Tree()
        self.add(tree)
        self.play(GrowingTree(tree), rate_func=linear, run_time=3)
        self.wait()