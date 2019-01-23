import numpy as np
import healpy as hp

nside = 1024
npix = hp.nside2npix(nside)
ipix = np.arange(npix)

theta, phi = hp.pix2ang(nside, ipix)
ra = np.rad2deg(phi)
dec = 90. - np.rad2deg(theta)

data = np.stack((ipix, ra, dec), axis=-1)

nfile = 100 # number of files, should be the same as the number of jobs in job array
nline = int(npix / nfile)

for i in range(nfile-1):
    fn = './ra_dec_files/radec_{0:0>2}.npy'.format(i)
    np.save(fn, data[i*nline : (i+1)*nline])

fn = './ra_dec_files/radec_{0:0>2}.npy'.format(nfile-1)
np.save(fn, data[(nfile-1)*nline:])

