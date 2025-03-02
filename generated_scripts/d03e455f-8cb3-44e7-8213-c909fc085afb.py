from manim import *

class RotatingCube(ThreeDScene):
    def construct(self):
        # Create a 3D cube
        cube = Cube()

        # Set the camera to a 3D perspective
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # Add the cube to the scene
        self.add(cube)

        # Rotate the cube
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(5)