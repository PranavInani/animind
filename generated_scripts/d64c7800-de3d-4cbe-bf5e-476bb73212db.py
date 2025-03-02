from manim import *

class RotatingCube(ThreeDScene):
    def construct(self):
        # Create a 3D cube
        cube = Cube()

        # Set the rotation speed
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(cube)

        # Rotate the cube
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(5)

        # Keep the animation running
        self.make_static_3d_scene()

        # Animate the cube
        self.play(Rotate(cube, angle=10 * PI, about=[0, 0, 1], run_time=2),
                  Rotate(cube, angle=10 * PI, about=[0, 1, 0], run_time=2),
                  Rotate(cube, angle=10 * PI, about=[1, 0, 0], run_time=2))

        # Keep the animation running
        self.wait(5)