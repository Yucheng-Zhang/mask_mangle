#!/bin/bash
#
#SBATCH --job-name=run_masks
#SBATCH --mail-type=END
#SBATCH --mail-user=yz4035@nyu.edu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=2GB
#SBATCH --time=48:00:00
#SBATCH --output=job_arr/masks_%A_%a.out
#SBATCH --error=job_arr/masks_%A_%a.err

module purge
module load gsl/intel/2.3
module load gcc/6.3.0
module load anaconda2/4.3.1
source activate py2

code_repo=/home/yz4035/local/mask_mangle

MDIR=/scratch/yz4035/make_mask_ja

cd $MDIR

in_mask_n=input/mask_DR14_QSO_N.ply
in_mask_s=input/mask_DR14_QSO_S.ply

python $code_repo/make_masks_ja.py -taskid $SLURM_ARRAY_TASK_ID -mask_n $in_mask_n -mask_s $in_mask_s

