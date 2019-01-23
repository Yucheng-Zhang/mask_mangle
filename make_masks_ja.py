'''
Make masks in job array.
'''
import numpy as np
import healpy as hp
import mangle as mg
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Make masks in job array.')
    parser.add_argument('-mask_n', default='',
                        help='Input north ploygon mask file')
    parser.add_argument('-mask_s', default='',
                        help='Input south ploygon mask file')
    parser.add_argument('-taskid', type=int, default=-
                        1, help='Task ID in job array')

    args = parser.parse_args()

    mask_n = mg.Mangle(args.mask_n)
    mask_s = mg.Mangle(args.mask_s)

    radec_fn = './ra_dec_files/radec_{0:0>2}.npy'.format(args.taskid)

    data = np.load(radec_fn)
    ipix = data[:, 0]
    l = data[:, 1]
    b = data[:, 2]

    r = hp.Rotator(coord=['G', 'C'])

    theta_gal = np.deg2rad(90. - b)
    phi_gal = np.deg2rad(l)
    theta_equ, phi_equ = r(theta_gal, phi_gal)
    ra = np.rad2deg(phi_equ)
    dec = 90. - np.rad2deg(theta_equ)

    w = np.zeros(len(ipix))
    for i in range(len(ipix)):
        if b[i] > 0.:
            w[i] = mask_n.weight(ra[i], dec[i])
        else:
            w[i] = mask_s.weight(ra[i], dec[i])

    data = np.column_stack((ipix, w))
    fn = './mask_files/masks_{0:0>2}.npy'.format(args.taskid)
    np.save(fn, data)
