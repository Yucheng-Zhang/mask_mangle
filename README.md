# make mask with mangle

Two methods are included.

## one step

- `make_mask.py` is parallelized with `multiprocessing`
 - run `python make_mask.py --help` to see all input options
- `run_mask.sh` shows how to use

## job array

Make mask with job array. I prefer to keeping codes and running directories seperately.

### step
- Make directories: `ra_dec_files`, `mask_files`, `job_arr`, `input`, `output` inside the directory (denote as [d1]) where you will run the code.
- Put the input polygon files in the `input` directory.
- Copy `*_ja.sh` to [d1], and change `code_repo` to the path where you keep the codes.
- Modify and run `bash make_radec_ja.sh`.
- Modify and run `sbatch --array=0-99 run_mask_ja.sh`
- Modify and run `bash add_masks_ja.sh`
