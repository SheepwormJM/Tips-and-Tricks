Use gffread to do this. See helpful comment on biostars: https://www.biostars.org/p/9571156/ 

1. Download the reference assembly in fasta format
2. Get your gff file
3. Install gffread (https://biocontainers.pro/tools/gffread)



```
gffread -g Genome.fa -y ProteinsOutput.fa YourGFF.gff

gffread -g ./REF.fa -y TtTr.fasta Tt.gff3

sed 's/CM052060\.1/Ttru_Chr1/g' GCA_028476895.1_ASM2847689v1_genomic.fna | sed 's/CM052061\.1/Ttru_Chr2/g' | sed 's/CM052062\.1/Ttru_Chr3/g' > REF.fa
```
