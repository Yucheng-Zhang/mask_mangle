#!/bin/bash
#
#SBATCH --job-name=mask
#SBATCH --mail-type=END
#SBATCH --mail-user=yz4035@nyu.edu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=20
#SBATCH --mem=64GB
#SBATCH --time=48:00:00
#SBATCH --output=./jobs/mask_job_%j.out
#SBATCH --error=./jobs/mask_job_%j.err

module purge
module load gsl/intel/2.3
module load gcc/6.3.0
module load anaconda2/4.3.1
source activate py2

MDIR=/scratch/yz4035/make_mask

cd $MDIR

code_repo=/home/yz4035/local/mask_mangle

fn=input/mask_DR14_LRG_N.ply
fs=input/mask_DR14_LRG_S.ply
outf=output/mask_DR14_LRG_nside_1024_test.fits

python $code_repo/make_mask.py -nside 1024 -mask_n $fn -mask_s $fs -ncpu 20 -outmask $outf

