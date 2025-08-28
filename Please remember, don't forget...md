# Merging two bam files for the same sample
If you have sequenced a sample twice and want to combine the bam files REMEMBER: If they were made from the same library then you want to MMR - Merge, Mark Duplicates and then Remove duplicates. This will find reads that are duplicates but would be retained in a single bam file. 

# awk
If you do not use ```BEGIN``` then it can strangely both skip and act upon the top row of your file simultaenously - outputting additional columns/counting etc with it, but equally not seeing it as a line with field separators.
