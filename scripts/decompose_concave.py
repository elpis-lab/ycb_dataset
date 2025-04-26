"""Used to decompose objects into near convex parts with V-HACD"""

import trimesh
import os


# Find the center of mass of the object
def save_to_obj(file_name):
    """Save stl file into obj files"""
    name, ext = os.path.splitext(file_name)
    obj_file_name = name + ".obj"
    mesh = trimesh.load(file_name)
    mesh.export(obj_file_name)
    return obj_file_name


def do_vhacd(filename, outfile, debug=False, **kwargs):
    try:
        mesh = trimesh.load(filename)
        convex_list = mesh.convex_decomposition(**kwargs)
        convex = trimesh.util.concatenate(convex_list)
        convex.export(outfile)

    except ValueError:
        print("No direct VHACD backend available, trying pybullet")

        try:
            import pybullet as p

            p.vhacd(filename, outfile, "vhacd_log.txt", **kwargs)
        except ModuleNotFoundError:
            print(
                +"\nERROR - pybullet module not found: "
                + "If you want to do convex decomposisiton, "
                + "make sure you install pybullet (https://pypi.org/project/pybullet) "
                + "or install VHACD directly (https://github.com/mikedh/trimesh/issues/404)"
                + "\n"
            )
            raise


def decompose(file_name, force_decompose, suffix="vhacd", **kwargs):
    """Decompose objects into near convex parts with vhacd with PyBullet"""
    file_extension = os.path.splitext(file_name)[1]
    if file_extension == ".stl":
        obj_file_name = save_to_obj(file_name)
    elif file_extension == ".obj":
        obj_file_name = file_name
    else:
        raise ValueError(
            "Needs to be an STL or OBJ to perform concave decomposition"
        )

    # Only run a decomposition if one does not exist, or if the user forces an overwrite
    out_file = obj_file_name.replace(".obj", "_" + suffix + ".stl")
    if not os.path.exists(out_file) or force_decompose:
        do_vhacd(obj_file_name, out_file, **kwargs)
    else:
        print("Skip as it already exists and overwriting is disabled")


# Perform concave decomposition of the entire library
# Loop for subfolders
force_decompose = True
decompose_resolution = 10000  # default 4e5
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
object_folder = "ycb"

suffix = "vhacd"

curr_dir = root_dir + "/" + object_folder + "/"
for subdir in os.listdir(curr_dir):
    curr_path = os.path.join(curr_dir, subdir)
    # HACK special for ycb
    if object_folder == "ycb":
        curr_path = os.path.join(curr_path, "google_16k")
    if not os.path.isdir(curr_path):
        continue

    # Loop through all the model obj/stl files
    for f in os.listdir(curr_path):
        curr_file = os.path.join(curr_path, f)

        # Skip non stl/obj files
        if not os.path.isfile(curr_file) or not (
            f.endswith(".stl") or f.endswith(".obj")
        ):
            continue
        # Skip the files that ends with suffix
        if f.endswith(suffix + ".stl") or f.endswith(suffix + ".obj"):
            continue

        print("Decomposing", subdir)
        file_name = os.path.join(curr_path, f)
        decompose(
            file_name,
            force_decompose,
            suffix=suffix,
            resolution=decompose_resolution,
        )
