1. Using subset in R.

**Note that the default is to ALSO exclude any NA containing rows...**

Can get around this by specifying to keep them. 
```
# For ordinary vectors, the result is simply ‘x[subset & !is.na(subset)]’
subset(df1, Height < 40 | is.na(Height))
```

2. Using awk with column headers:
```
awk '
NR==1 {
    for (i=1; i<=NF; i++) {
        f[$i] = i
    }
}
{ print $(f["foo"]), $(f["baz"]) }
' file
```
Note that the above doesn't seem to work well when trying (at least the way I just have) to select rows conditionally. 

However, to check have printed out the correct headers can add ```NR == 1 ||``` to the conditional, and this will also nicely retain the header line: 

```
awk 'BEGIN {OFS=FS="\t"} (NR == 1 || $1 == "qqPsoOvis1.1_s07" && $2 > 2559925 && $2 < 2577022) {print $1,$2,$20}' Povis_WGS_CROSS_mmp2_s1-53_2026Nov24.depth > MLSUS_s07_2559925-2577022_2026Nov24.depth
```


3. Using grep to pull out lines containing a string match:
```
grep -e 'keep' file.txt > new_file.txt
```
