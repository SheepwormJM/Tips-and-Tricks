## Sed... :) 
```
sed 's/old_thing/new_thing/g' file > new_file
```

To remove any character up to a point, and then any character after a point:
```
sed 's/.*\///g' list_loci.txt | sed 's/_BTUB.*//g' > out
# The first removes anything (.*) up to the last / (escaped by the \ before it)
# The next removes _BTUB and anything after it (.*)
```

Note, when copy and paste, or with some files, get multiple spaces, not a tab (check with cat -T). To replace multiple spaces with a single space and then all single spaces with a tab do the following: 

```
# Note that there are TWO spaces in the first one!
sed 's/  */ /g' filename | sed 's/ /\t/g' > new_filename
```


## In R, can use gsub: 
```
# gsub https://endmemo.com/r/gsub.php
# gsub(pattern, replacement, x, ignore.case = FALSE, perl = FALSE, fixed = FALSE, useBytes = FALSE)

win_melt_FA$variable.new<-gsub("FA.FB_C_L","CTL", win_melt_FA$variable.new)
```
