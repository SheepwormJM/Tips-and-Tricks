## Re-order columns in awk, when there are many columns!
```
awk '{OFS="\t"}{ for (i=4; i<=NF; i++)   printf $i "\t"}{print $1, "\t", $2,"\t", $3}' old_file > new_file
```
This will output my file with tabs between each column. Note that if you have
```
print $i
```
rather than
```
printf $i
```
you get a new line for every single entry.........

So it is saying:
1. Output my file with tabs between each column (OFS)
2. Starting at column 4, until you reach the end of the columns in the file, print that column
3. Separate each column with a tab (the OFS didn't seem to work without it, so it may be irrelevant in the script above)
4. Print columns 1, 2 and 3 after the last column printed. Again, with tabs between them.

## Replace multiple spaces, or tabs etc with a single one:
```
# Replace two or more tabs with a single tab. 
sed 's/\t\+/\t/g' header_ratio > header_new

# Replace two or more spaces with a single tab:
sed 's/ \+/\t/g' header_ratio > header_new
```

## Obtain just certain columns quickly using cut

Note that it sees a tab at the start of a line as a column, even though using awk '{print NF}' does not....
```
cut -f 1-29 file > tmp_rank_cols
cut -f 28-30 file > tmp_pi_cols
cut -f 28-29,31- file > tmp_ratio_cols
```
