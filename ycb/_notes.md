# Notes

- The mass of each object is manually set based on the provided mass [form](http://www.ycbbenchmarks.com/wp-content/uploads/2015/09/object-list-Sheet1.pdf). The inertia of all objects are simply diagonal matrix with value 1e-3.

- All the texture images are compressed to 80% JPG with image size unchanged. This should improve simulation performance and save space without affecting the vision pipeline.

- This repository only includes models with Google 16K. The other models, shown as below, are not included.

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

    