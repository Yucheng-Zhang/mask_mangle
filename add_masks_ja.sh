#!/bin/bash

code_repo=/home/yz4035/local/mask_mangle

out_mask_file=output/mask_DR14_QSO_nside_1024_ja.fits

python $code_repo/add_masks_ja.py -nfile 100 -outmask $out_mask_file

