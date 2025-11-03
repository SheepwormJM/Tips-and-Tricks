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

# Awk with if and else, not tested:
```
awk '{OFS="\t"}
{ if ($3=="gene"){
    gsub("^","gene_id=",$9);
    gsub("$",";",$9);
    #print
} else if($3=="transcript"){
    geneID=$9;
    transcriptID=$9;
    gsub("..*",";",geneID);
    gsub("^","gene_id=",geneID);
    gsub("^","transcript_id=",transcriptID);
    $9=geneID" "transcriptID";";
    print $9
} else {
    print
} 
}'
```
