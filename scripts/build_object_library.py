"""Build URDF for objects.
Scripts from https://github.com/harvard-microrobotics/object2urdf
"""

import os
from object_urdf import ObjectUrdfBuilder

# Build entire libraries of URDFs
# This is only suitable for objects built with single obj/stl file
# Models such as robots or articulated objects will not work properly

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
object_folder = root_dir + "/ycb"

builder = ObjectUrdfBuilder(object_folder)
builder.build_library(
    force_overwrite=False,
    decompose_concave=True,  # build *_vhacd.obj files
    force_decompose=False,  # overwrite decomposed files
    center="mass",  # object center is at mass center
    decompose_resolution=10000,  # resolution for vhacd (default 4e5)
)
