import os

#https://slurm.schedmd.com/squeue.html
os.system('sbatch batch.src') 
os.system('squeue -u username')