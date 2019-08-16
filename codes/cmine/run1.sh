#!/bin/bash
#SBATCH -A research
#SBATCH --qos=medium
#SBATCH -n 4
#SBATCH --mem-per-cpu=2048
#SBATCH --time=3-00:00:00
#SBATCH --mail-type=END
python run1.py
