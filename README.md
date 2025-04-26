# ycb_dataset

YCB dataset with urdf files. Ready to be used in different simulations such as PyBullet.

## Usage

Have **ycb** folder in your project directory.

For convenience, the locations of urdf file can be found with \_\_init\_\_.py of **ycb** directly. An example is

```
from ycb import YCB
cracker_box_urdf = YCB["cracker_box"]
```

## Procedure

Here is the procedure of how this repository is made.

- The dataset is downloaded from the [YCB dataset website](https://www.ycbbenchmarks.com/) with script `download_ycb_dataset.py` provided by [ycb-tools](https://github.com/sea-bass/ycb-tools/tree/main). Only textured models with Google 16K are used.
- The urdf files are generated with scripts `build_object_library.py` and `object_urdf.py` provided by [object2urdf](https://github.com/harvard-microrobotics/object2urdf). Convex decomposition is done with `trimesh`.
- The mass of each object is manually set based on the provided mass [form](http://www.ycbbenchmarks.com/wp-content/uploads/2015/09/object-list-Sheet1.pdf). The inertia of all objects are simply diagonal matrix with value 1e-3.
- All the texture images are compressed to 80% JPG with image size unchanged with `image_compressor.py`. This should improve simulation performance and save space without affecting the vision pipeline.

## Models not included

This repository only includes models with Google 16K. The other models, shown as below, are not included.

- models only with rgbd, not google_16k:
  - 001
  - 041
  - 049
  - 072-f
  - 072-h
  - 072-i
  - 072-j
  - 072-k
  - 073-h
  - 073-i
  - 073-j
  - 073-k
  - 073-l
  - 073-m
- low-quality models:
  - 023
  - 039
  - 046
  - 047
  - 063-c
  - 063-d
  - 063-e
  - 063-f
  - 072-g
