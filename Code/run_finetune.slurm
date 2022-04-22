#!/bin/bash

#SBATCH --job-name=prompting-gpt
#SBATCH --open-mode=append
#SBATCH --output=/scratch/${USER}/%j_%x.out
#SBATCH --error=/scratch/${USER}/%j_%x.err
#SBATCH --export=ALL
#SBATCH --account=ds_ga_1012_2022sp
#SBATCH --partition=n1s8-p100-1
#SBATCH --time=04:00:00
#SBATCH --gres=gpu:1
#SBATCH --mem=25G
#SBATCH -c 4
#SBATCH --mail-user=<yl5865@nyu.edu>
#SBATCH --mail-type=All
#SBATCH --requeue

## Run your hyperparameter search in a singularity container. Remember to
## activate your Conda environment in the container before running your Python script.
singularity exec --nv --bind /scratch/$USER --overlay /scratch/$USER/overlay-25GB-500K.ext3:ro /scratch/$USER/cuda11.4.2-cudnn8.2.4-devel-ubuntu20.04.3.sif /bin/bash -c "
source /ext3/env.sh
python run_finetune.py /scratch/yl5865 /scratch/yl5865/ds_config.json
"
