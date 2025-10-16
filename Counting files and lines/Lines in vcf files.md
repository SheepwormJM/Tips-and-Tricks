This counts the number of lines in a vcf file, first excluding all those with a # at the start - in other words header lines. It also will print out the filename along with the number of lines. 
```
for i in *.vcf ;
do
grep -v '^#' $i | wc -l ${i};
done
```
