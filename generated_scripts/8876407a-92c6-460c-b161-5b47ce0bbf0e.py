from manim import *

class RotatingCube(ThreeDScene):
    def construct(self):
        # Create a 3D cube
        cube = Cube(color=RED)

        # Add the cube to the scene
        self.add(cube)

        # Rotate the cube
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(5)