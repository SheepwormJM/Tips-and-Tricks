Here is how to make each line the same length - the same number of columns using awk. 

```
awk 'BEGIN {OFS=FS="\t"} 
       NR==1 {max=NF} 
             {for(i=NF+1;i<=max;i++) $i="null"}1' file > file_new ;
```



For a set of files called Col6 to Col14:
```
for NUMBER in {6..14} ;
do
awk 'BEGIN {OFS=FS="\t"} 
       NR==1 {max=NF} 
             {for(i=NF+1;i<=max;i++) $i="null"}1' Col$NUMBER > Col${NUMBER}_new ;
done
```
