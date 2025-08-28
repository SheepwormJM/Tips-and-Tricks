To import:
```
df<-read.table("filename.txt", header=T, sep="\t", na.strings = "nan")
```

To export: 
```
write.table(df, file="new_file_name.txt", row.names=FALSE, sep="\t", quote= FALSE)
```
