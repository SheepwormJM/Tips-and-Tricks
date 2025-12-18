From https://unix.stackexchange.com/questions/561577/awk-print-from-nth-column-to-last
```
awk '{$1=$2=$3=""; $0=$0; $1=$1; print}' file
```

The following prints all except the first column. Note that this method is still inserting a 'column 1' but it is empty, so you get three tabs in a row and I then use sed to remove two of them.
```
for i in avg*Minimap*;
do
awk '{OFS="\t"} {print FILENAME , $1="", $0}' ${i} | sed 's/\t\t//g' > newfile_out ;
done
```
