This counts the number of lines in a vcf file, first excluding all those with a # at the start - in other words header lines. It will not print out the filename along with the number of lines, but they are being output in alphanumerical order I think. 
```
grep -v '^#' $i | wc -l 
```
