## How to get a sum of mpileup sync counts by line

This script will do the following:

- It will loop through the columns 4 to 30 (in the sync file there are 30 columns, the first three are concerned with the position and the SNP allele, the rest have the per sample data
- It will then print each column, print the first 4 bases, and the deletions from that column and finally it will sum the counts of those 4 bases and deletions (so it ignores N's).
- NICE! :D
```
# awk -v assigns a value to a variable before awk starts
for i in {4..30}; 
do
    cat file.sync | \
    awk -v col=$i 'BEGIN {FS=OFS="\t"} {print $col }' | awk 'BEGIN {FS=OFS=":"} {print $1,$2,$3,$4,$6}' | sed 's/\:/+/g' | bc > sum_col${i} ;
done &
```
(Note, the columns in the sync were made by popoolation2 - the four bases, then N, then deletions).
