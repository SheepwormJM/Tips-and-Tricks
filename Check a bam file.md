## Check if it is truncated 
_Note - this checks the header and the tail, it isn't checking the contents._
```
samtools quickcheck -v *.bam > bad_bams.fofn   && echo 'all ok' || echo 'some files failed check, see bad_bams.fofn'
```
