## Sed... :) 
```
sed 's/old_thing/new_thing/g' file > new_file
```

## In R, can use gsub: 
```
# gsub https://endmemo.com/r/gsub.php
# gsub(pattern, replacement, x, ignore.case = FALSE, perl = FALSE, fixed = FALSE, useBytes = FALSE)

win_melt_FA$variable.new<-gsub("FA.FB_C_L","CTL", win_melt_FA$variable.new)
```
