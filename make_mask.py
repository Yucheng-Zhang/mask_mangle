'''
Make mask map with mangle polygon data files.
'''
import numpy as np
import healpy as hp
import mangle as man
import multiprocessing as mp
import argparse


def OnePixel(i):
    if b[i] > 0.:
        return mask_n.weight(ra[i], dec[i])
    else:
        return mask_s.weight(ra[i], dec[i])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Make mask map with mangle polygon data files.')
    parser.add_argument('-mask_n', default='',
                        help='input north polygon mask file')
    parser.add_argument('-mask_s', default='',
                        help='input south polygon mask file')
    parser.add_argument('-nside', type=int, default=128,
                        help='nside for the output mask map')
    parser.add_argument('-ncpu', type=int, default=0,
                        help='''number of cpus for multiprocessing\n
                        0: detect with cpu_count''')
    parser.add_argument('-outmask', default='',
                        help='output mask map file name')

    args = parser.parse_args()

#    global mask_n, mask_s, ra, dec, b

    mask_n = man.Mangle(args.mask_n)
    mask_s = man.Mangle(args.mask_s)

    r = hp.Rotator(coord=['G', 'C'])

    nside = args.nside
    npix = hp.nside2npix(nside)
    print('npix = {0:d}'.format(npix))

    theta_gal, phi_gal = hp.pix2ang(nside, np.arange(npix))

    theta_equ, phi_equ = r(theta_gal, phi_gal)
    ra = np.rad2deg(phi_equ)
    dec = 90. - np.rad2deg(theta_equ)

    b = 90. - np.rad2deg(theta_gal)

    if args.ncpu == 0:
        num_cpus = mp.cpu_count()
    else:
        num_cpus = args.ncpu

    print('Number of CPUs: {0:d}'.format(num_cpus))

    pool = mp.Pool(num_cpus)
    mask = pool.map(OnePixel, [i for i in range(npix)])
    pool.close()
    pool.join()

    mask = np.array(mask)
    mask[np.where(mask == -1)] = 0.

    hp.write_map(args.outmask, mask)
