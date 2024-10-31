# How many columns?
### ... and are there the same number on each line? 
```
awk '{print NF}' file | uniq > nf_file
```
