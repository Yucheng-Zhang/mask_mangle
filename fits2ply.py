'''
Polygon file: .fits -> .ply
'''
import numpy as np
from astropy.io import fits
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Polygon file: .fits -> .ply')
    parser.add_argument('-fits', type=str, default='', help='input fits file')
    parser.add_argument('-ply', type=str, dedault='', help='output ply file')
    args = parser.parse_args()


def read_fits(fn):
    '''Read in the fits file.'''
    hdu = fits.open(fn)
    data, header = hdu[1].data, hdu[1].header
    npoly = len(data)
    names = data.dtype.names
    formats = data.formats


if __name__ == "__main__":
    pass
