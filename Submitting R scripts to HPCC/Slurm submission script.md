As well as your R script, you need to write a slurm submission script to run your rscript. 

Note - you want to first install any packages that you need into the R environment that you will use. I.e. first, load the R module that you want (the version). Then, in R, install your packages. Then quit and submit your script. If you've previously installed the packages in the R version you want to use then you can skip this bit.
```
#!/bin/bash -l

############# SLURM SETTINGS #############
#SBATCH --job-name=test_R_script       # some descriptive job name of your choice
#SBATCH --output=%x-%J.out      # output file name will contain job name + job ID
#SBATCH --error=%x-%J.err       # error file name will contain job name + job ID
#SBATCH --time=0-2:00:00       # time limit for the whole run, in the form of d-hh:mm:ss, also accepts mm, mm:ss, hh:mm:ss, d-hh, d-hh:mm
#SBATCH --mem=1G                # memory required per node, in the form of [num][M|G|T]
#SBATCH --ntasks=1              # number of Slurm tasks to be launched, increase for multi-process runs ex. MPI
#SBATCH --cpus-per-task=1       # number of processor cores to be assigned for each task, default is 1, increase for multi-threaded runs
#SBATCH --ntasks-per-node=1     # number of tasks to be launched on each allocated node

############# LOADING MODULES (optional) #############
#module load apps/xxx
#module load libs/xxx

module load R/4.4.2

############# MY CODE #############
# pwd = /home/jenni/data_folder/working_folder/  # This is just here for my sanity to tell me where I was working when I was using it

# Rscript path/file_r_script.R argument_1 argument_2 .... argument_n
Rscript /home/jenni/data_folder/working_folder/trial_r_script.R /home/jenni/data_folder/working_folder/directory_with_my_input_file/ my_input_file.txt my_output_file_name 
```
Save the above, make it executable and submit:
```
sbatch ./run_R_script.sh
```
