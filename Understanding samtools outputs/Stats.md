For many of the samtools stats outputs the stats are referring ONLY to primary alignments - supplementary/secondary alignments are ignored. 

However, this is not true of all the stats! 

The below was obtained from a file containing only supplementary alignments - these are included in the total bases mapped and error rate:
```
# Summary Numbers. Use `grep ^SN | cut -f 2-` to extract this part.
SN      raw total sequences:    0       # excluding supplementary and secondary reads
SN      filtered sequences:     0
SN      sequences:      0
SN      is sorted:      1       # sorted by coordinate
SN      1st fragments:  0
SN      last fragments: 0
SN      reads mapped:   0
SN      reads mapped and paired:        0       # paired-end technology bit set + both mates mapped
SN      reads unmapped: 0
SN      reads properly paired:  0       # proper-pair bit set
SN      reads paired:   0       # paired-end technology bit set
SN      reads duplicated:       0       # PCR or optical duplicate bit set
SN      reads MQ0:      0       # mapped and MQ=0
SN      reads QC failed:        0
SN      non-primary alignments: 0
SN      supplementary alignments:       232
SN      total length:   0       # ignores clipping
SN      total first fragment length:    0       # ignores clipping
SN      total last fragment length:     0       # ignores clipping
SN      bases mapped:   0       # ignores clipping
SN      bases mapped (cigar):   10020   # more accurate
SN      bases trimmed:  0
SN      bases duplicated:       0
SN      mismatches:     27      # from NM fields
SN      error rate:     2.694611e-03    # mismatches / bases mapped (cigar)
SN      average length: 0
SN      average first fragment length:  0
SN      average last fragment length:   0
SN      maximum length: 101
SN      maximum first fragment length:  101
SN      maximum last fragment length:   101
SN      average quality:        0.0
SN      insert size average:    0.0
SN      insert size standard deviation: 0.0
SN      inward oriented pairs:  0
SN      outward oriented pairs: 0
SN      pairs with other orientation:   0
SN      pairs on different chromosomes: 0
SN      percentage of properly paired reads (%):        0.0

```

However, secondary read alignments are NOT:
```
# Summary Numbers. Use `grep ^SN | cut -f 2-` to extract this part.
SN      raw total sequences:    0       # excluding supplementary and secondary reads
SN      filtered sequences:     0
SN      sequences:      0
SN      is sorted:      1       # sorted by coordinate
SN      1st fragments:  0
SN      last fragments: 0
SN      reads mapped:   0
SN      reads mapped and paired:        0       # paired-end technology bit set + both mates mapped
SN      reads unmapped: 0
SN      reads properly paired:  0       # proper-pair bit set
SN      reads paired:   0       # paired-end technology bit set
SN      reads duplicated:       0       # PCR or optical duplicate bit set
SN      reads MQ0:      0       # mapped and MQ=0
SN      reads QC failed:        0
SN      non-primary alignments: 16
SN      supplementary alignments:       0
SN      total length:   0       # ignores clipping
SN      total first fragment length:    0       # ignores clipping
SN      total last fragment length:     0       # ignores clipping
SN      bases mapped:   0       # ignores clipping
SN      bases mapped (cigar):   0       # more accurate
SN      bases trimmed:  0
SN      bases duplicated:       0
SN      mismatches:     0       # from NM fields
SN      error rate:     0.000000e+00    # mismatches / bases mapped (cigar)
SN      average length: 0
SN      average first fragment length:  0
SN      average last fragment length:   0
SN      maximum length: 0
SN      maximum first fragment length:  0
SN      maximum last fragment length:   0
SN      average quality:        0.0
SN      insert size average:    0.0
SN      insert size standard deviation: 0.0
SN      inward oriented pairs:  0
SN      outward oriented pairs: 0
SN      pairs with other orientation:   0
SN      pairs on different chromosomes: 0
SN      percentage of properly paired reads (%):        0.0
```
