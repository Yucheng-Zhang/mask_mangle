# make mask with mangle

Two methods are included.

## one step

- `make_mask.py` is parallelized with `multiprocessing`
 - run `python make_mask.py --help` to see all input options
- `run_mask.sh` shows how to use

## job array (need update)

Make mask with job array.

### step
- make two directories `ra_dec_files` and `mask_files`
- `sbatch --array=0-99 run_mask_ja.sh`
