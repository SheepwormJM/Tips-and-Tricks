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
