## To loop through a set of files with another loop within that!
How to run a 'while read lines in file do x' loop within another loop to  rattle through different files in a directory
```
for i in Ce*list.txt; do

while read NAME;
do
samtools faidx /nfs/users/nfs_j/jm62/scratch/Orthofinder/proteomes/WBPS18_Tci2_wsi2.4_Jan2024_analysis/primary_transcripts/C_elegans.fa ${NAME} >> ${i}.aa.fa; done < /nfs/users/nfs_j/jm62/scratch/Orthofinder/proteomes/WBPS18_Tci2_wsi2.4_Jan2024_analysis/primary_transcripts/OrthoFinder/Results_Apr16/Phylogenetic_Hierarchical_Orthogroups/${i} ;

done
```
