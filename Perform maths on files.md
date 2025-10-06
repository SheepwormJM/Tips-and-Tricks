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

## Overcome dividing by zero with awk

If you are dividing one column by another, and the divisor is a zero (e.g. 2/0) then awk throws up an error and terminates the process. 

To simply overcome this, and output zero, you can use a TERNERY operator (?) to check if something is true or not:
```
# Original -> error
awk 'BEGIN {OFS=FS="\t"} {print ($1 / $2) }' file_in > file_out_fails

# Check if $2 value is zero before attempting
awk 'BEGIN {OFS=FS="\t"} {print (($2 == 0) ? 0: ($1 / $2)) }' file_in > file_out_works

# Note that the above will output 0 if $2 = 0.


# You can change what is output, e.g. the following will output Col2is0
awk 'BEGIN {OFS=FS="\t"} {print (($2 == 0) ? "Col2is0" : ($1 / $2) ) }' file_in > file_out_works

# However, the " are needed - otherwise the output line is still output, but is empty
awk 'BEGIN {OFS=FS="\t"} {print (($2 == 0) ? Col2is0 : ($1 / $2)) }' file_in > file_out_works

# Note that if it has NaN rather than 0 in $2 then the script will fail.

# But can overcome and put whatever you like!
# For example - the following will check if either column 3 or column 4 is 0 and, if either is, will output that "Acolumnis0"
awk 'BEGIN {OFS=FS="\t"} {print (($1 == 0 || $2 == 0) ? "Acolumnis0" : ($1 / $2) ) }' file_in > file_out_works
```
https://www.thegeekstuff.com/2010/02/awk-conditional-statements/

https://quickref.me/awk.html
