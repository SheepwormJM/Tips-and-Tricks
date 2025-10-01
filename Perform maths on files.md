## Loop through rows and average

```
# This following script (obtained from https://unix.stackexchange.com/questions/396335/averaging-over-many-rows-of-data) will output the average for the number of rows N.
# If there are fewer than N rows left (the NR % N ==0) bit then it will not put out anything for those lines. So, if I select it to average over 1000 rows, then it would ignore the last 999 rows of data (or less).
 
awk '
BEGIN {
    N = 10000;
}
{
    for(i = 1; i <= NF; i++) {
        arr[i] += $i;   
    }
}
NR % N == 0 {
    for(i = 1; i <= NF; i++) {
        printf "%s ", arr[i] / N;
    }
    print "";
    delete arr;

}' tmp > new_tmp
```

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

Got the idea from here: https://www.theunixschool.com/2012/09/find-sum-all-numbers-columns-in-line-linux.html which has other simple tips too.
