'''
Make mask.
'''
import numpy as np
import healpy as hp
import mangle as man
import multiprocessing as mp

cat_path = './input/'

mask_n = man.Mangle(cat_path + 'mask_DR14_LRG_N.ply')
mask_s = man.Mangle(cat_path + 'mask_DR14_LRG_S.ply')

r = hp.Rotator(coord=['G', 'C'])

nside = 128
npix = hp.nside2npix(nside)
print('npix = {0:d}'.format(npix))

theta_gal, phi_gal = hp.pix2ang(nside, np.arange(npix))

theta_equ, phi_equ = r(theta_gal, phi_gal)
ra = np.rad2deg(phi_equ)
dec = 90. - np.rad2deg(theta_equ)

b = 90. - np.rad2deg(theta_gal)

def OnePixel(i):
    if i % 100 == 0:
        print('{0:.2f} %'.format(100.*i/npix))
    if b[i] > 0.:
        return mask_n.weight(ra[i], dec[i])
    else:
        return mask_s.weight(ra[i], dec[i])


num_cpus = mp.cpu_count()
print('Num of CPUs: {0:d}'.format(num_cpus))

pool = mp.Pool(num_cpus)
mask = pool.map(OnePixel, [i for i in range(npix)])
pool.close()
pool.join()

#for i in range(npix): OnePixel(i)

mask = np.array(mask)
mask[np.where(mask==-1)] = 0.

hp.write_map('output/mask_DR14_LRG_nside_{0:d}_para.fits'.format(nside), mask)

