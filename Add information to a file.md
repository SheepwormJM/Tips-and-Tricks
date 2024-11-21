# Add line numbers: 
### ...which can handily give a rank after first sorting a file:
- Note, these are always added in a new first column/start of the file.

Nice bit of info here: https://www.geeksforgeeks.org/nl-command-in-linux-with-examples/ 
```
cat file | sort -k 4 -n | nl > new_file
```

# Add text strings:

1. Using _awk_ in linux:
```
awk 'BEGIN {FS=OFS="\t"} {print $0, ($2 + 50000), "IVM"}' myfile > myfile_with_IVM_in_new_last_column
```

2. In R, using _paste_:
```
df9$addMe <- paste0("text to add", df9$addMe)
```

3. Using _sed_ in linux:
```
# This will add a tab and NA to the end of the line (denoted by $)
sed 's/$/\tNA/g' tmp3 > tmp4
```
# Add file name to files:
To get the filename in the first column of the file and to then cat (stick) lots of files together one after the other but without needing to write all the names...
```
for i in MEAN* ;
do
awk 'NR==1{print "file_name",$0;next} {print FILENAME , $0}' ${i} > tmp_${i} ;
done

mkdir MEAN_Pi
mv tmp* MEAN_Pi
cat MEAN_Pi/* > MEAN_Pi_chr_locus
```
