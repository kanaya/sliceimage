# sliceimage

Image slicer.

If you want to split an image into n equally-sized tiles, [image_slicer](https://pypi.org/project/image_slicer/) works better.

## Usage

```sh
python sliceimage.py --xstart {xstart} --ystart {ystart} --xstride {xstride} --ystride {ystride} --xoffset {xoffset} --yoffset {yoffset} --xsize {xsize} --ysize {ysize} input.png
```

![Options](options.jpg)

Note: Normally you don't need to set `xoffset` or `yoffset`.
