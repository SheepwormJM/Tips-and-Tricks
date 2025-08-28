# Subsample the file to extract only every 100th line.
```
awk 'NR % 100 == 0' file > new_file
```
