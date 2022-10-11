""" works on git checkpoint:  """
from turtle import fillcolor
from manim import *

from concept import obj_model
from behavior import utils, format

class Test(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES)

        pcd = obj_model.Point_Cloud("gallery/material/cube.obj")
        # pcd.lightup()
        pcd.rotate(90*DEGREES, RIGHT)
        
        mesh = obj_model.Mesh(
            "gallery/material/cube.obj",
            # sheen_factor=0.5,
        ).set_sheen(-0.3, DR)
        # mesh.lightup()
        mesh.rotate(90*DEGREES, RIGHT).next_to(pcd, RIGHT)

        self.add(pcd)
        self.add(mesh)
        self.begin_ambient_camera_rotation(rate=4)
        self.wait()


if __name__ == "__main__":
    with tempconfig({
        # "format": "png",
        # "transparent": True,
        # "output_file": "manim-",
        # "zero_pad": False,
        "frame_rate": 24,
        #"pixel_width": 2048,
        # "pixel_height": 1024,
        "preview": True,
    }):
        scenes = (
            Test(),
        )

        for scene in scenes:
            scene.render()