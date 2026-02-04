# In R: 
```
library(dplyr)

# Stack the tables one on top of the other (i.e. concatenate without the headers)
df3<-bind_rows(df,df2)

# Join tables together, side by side, merged, based on values in one or more columns
# For example... 
# Join the two tables, using the chrom, start and end positions.
# Note that for col1 = col2 it will assume col1 is in the first df and col2 is in the second
# By using all three it will ensure that only if they all match will it join, so it will not duplicate
# It will output the remaining columns in each df, but only the matching columns once

new<-inner_join(df,  df2, by=c("V1"="chrom","V2"="start","V3"="end"))

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
