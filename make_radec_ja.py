'''
Make radec files for job array.
'''
import numpy as np
import healpy as hp
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Make radec files for job array.')
    parser.add_argument('-nside', type=int, default=128,
                        help='nside for the mask map')
    parser.add_argument('-nfile', type=int, default=100,
                        help='''number of files for job array,
                        should be the same as the number of jobs in job array.''')

    args = parser.parse_args()

    nside = args.nside
    nfile = args.nfile

    npix = hp.nside2npix(nside)
    ipix = np.arange(npix)

    theta, phi = hp.pix2ang(nside, ipix)
    ra = np.rad2deg(phi)
    dec = 90. - np.rad2deg(theta)

    data = np.stack((ipix, ra, dec), axis=-1)

    nline = int(npix / nfile)

    for i in range(nfile - 1):
        fn = './ra_dec_files/radec_{0:0>2}.npy'.format(i)
        np.save(fn, data[i * nline: (i + 1) * nline])

        fn = './ra_dec_files/radec_{0:0>2}.npy'.format(nfile - 1)
        np.save(fn, data[(nfile - 1) * nline:])
