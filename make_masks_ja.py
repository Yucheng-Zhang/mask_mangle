import sys
import numpy as np
import healpy as hp
import mangle as mg

mask_n = mg.Mangle('./input/mask_DR14_LRG_N.ply')
mask_s = mg.Mangle('./input/mask_DR14_LRG_S.ply')

idx = sys.argv[1]
radec_fn = './ra_dec_files/radec_{0:0>2}.npy'.format(idx)

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
fn = './mask_files/masks_{0:0>2}.npy'.format(idx)
np.save(fn, data)

