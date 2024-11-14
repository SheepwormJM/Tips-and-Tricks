# In R: 
```
library(dplyr)

# Stack the tables one on top of the other (i.e. concatenate without the headers)
df3<-bind_rows(df,df2)
```

# In linux using cat:
To put two files together:
```
cat file1 file2 > new_file
```
To put together all the files starting with 'tmp'
```
mkdir MEAN_Pi
mv tmp* MEAN_Pi
cat MEAN_Pi/* > MEAN_Pi_chr_locus
```
