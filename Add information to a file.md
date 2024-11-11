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

3. In R, using _paste_:
```
df9$addMe <- paste0("text to add", df9$addMe)
```
