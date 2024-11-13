## Rename!

```
rename old_text new_text files

# The below will rename all .fastq files that have F1R1 in them - replacing the first occurance of F1R1 with Sample1
rename F1R1 Sample1  *.fastq
```
## Move...
Can use the ```mv``` to rename. 

Can use some combination of ls, sed, paste and mv etc to do lots all at once. 

e.g. 
```
ls *.fastq > file_list

cp file_list file_list2

sed 's/^/mv /g' file_list > tmp
sed 's/old_text/new_text/g' file_list2 > tmp2

paste tmp tmp2 > tmp3

# Then copy and paste the lines in tmp3 and renames all files by mv
```
