Use cpslit to split a single file into multiple files (see https://unix.stackexchange.com/questions/263904/split-file-into-multiple-files-based-on-pattern): 
```
NEEDLE=//
HAYSTACK=/users/jmi45g/project0005/EEID/ITS2_sequences_NCBI/
csplit -f splitfile_ $HAYSTACK /$NEEDLE/ "{$(($(grep -c -- $NEEDLE $HAYSTACK)-1))}"
for file in splitfile_*; do
    sed --in-place "s/$NEEDLE//" $file
done
```
You can then split the file into multiple files using a regular expression, in this case //. Be wary if it is present WITHIN your data!
```
csplit -f H_placei ./H_placei_ITS2_NCBI.gb  /^\/\// {*}

csplit -f H_similis ./H_similis_ITS2_NCBI.gb  /^\/\// {*}
```
The below will then allow you to pull out multiple lines from each file, keeping them together using strings. The ```/|``` is a command telling grep to look for 'a' OR 'b' on any given line to pull it out. 
```
for i in H_*[1-9] ;
do 
cat $i | grep -e 'ACCESSION\|SOURCE\|organism=\|geo_loc_name=\|host=\|isolation_source=\|dev' >> Useful_ITS2_info.txt ; 
done
```
