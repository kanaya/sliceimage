import argparse
import math
import os
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument('input', help='Input image file')
parser.add_argument('--xoffset', help='X offset', default=0)
parser.add_argument('--yoffset', help='Y offset', default=0)
parser.add_argument('--xstride', help='X stride', default=100)
parser.add_argument('--ystride', help='Y stride', default=100)
parser.add_argument('--xsize', help='Width', default=100)
parser.add_argument('--ysize', help='Height', default=100)
args = parser.parse_args()

filename = args.input
xoffset = int(args.xoffset)
yoffset = int(args.yoffset)
xstride = int(args.xstride)
ystride = int(args.ystride)
xsize = int(args.xsize)
ysize = int(args.ysize)

im = Image.open(filename)
w, h = im.size
m = math.floor((w-xoffset)/xstride)
n = math.floor((h-yoffset)/ystride)
bn, ext = os.path.splitext(os.path.basename(filename))

print('w == {}, h == {}, m == {}, n == {}'.format(w, h, m, n))

for y in range(n):
	for x in range(m):
		outfilename = '{}_{}_{}.png'.format(bn, x, y)
		xbegin = xoffset + x*xstride
		ybegin = yoffset + y*ystride
		xend = xbegin+xsize
		yend = ybegin+ysize
		print('Cropping from ({}, {}) to ({}, {}) and writing to {}'.format(xbegin, ybegin, xend, yend, outfilename))
		im.crop((xbegin, ybegin, xend, yend)).save(outfilename)
