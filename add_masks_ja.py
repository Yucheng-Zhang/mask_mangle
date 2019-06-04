'''
Merge masks from job array into one.
'''
import numpy as np
import healpy as hp
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Merge masks from job array into one.')
    parser.add_argument('-nfile', type=int, default=100,
                        help='number of masks files')
    parser.add_argument('-outmask', default='', help='output mask file name')
    args = parser.parse_args()

    mask = np.array([])

    for i in range(args.nfile):
        fn = './mask_files/masks_{0:0>3}.npy'.format(i)
        data = np.load(fn)
#        ipix = data[:, 0]
        mask = np.append(mask, data[:, 1])

    mask[np.where(mask == -1)] = 0

    hp.write_map(args.outmask, mask)
