import numpy as np
import healpy as hp

mask = np.array([])

for i in range(100):
    fn = './mask_files/masks_{0:0>2}.npy'.format(i)
    data = np.load(fn)
#    ipix = data[:, 0]
    mask = np.append(mask, data[:, 1])

mask[np.where(mask==-1)] = 0

hp.write_map('./output/mask_DR14_LRG_nside_1024_ja.fits', mask)

