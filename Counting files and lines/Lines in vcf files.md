This counts the number of lines in a vcf file, first excluding all those with a # at the start - in other words header lines. It will not print out the filename along with the number of lines, but they are being output in alphanumerical order I think. 
```
grep -v '^#' $i | wc -l 
```

However, this loop and paste command will create an output file that contains the number of lines without the header lines and the filename.
```
for i in *.vcf ;
do
echo ${i} >> filenames ;
grep -v '^#' $i | wc -l >> filelines ;
done
paste filelines filenames > file_summary
```
