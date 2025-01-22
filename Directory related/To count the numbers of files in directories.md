To count the numbers of files in directories:
```
find . -type f | cut -d"/" -f2 | uniq -c | sort -rn > files_in_directories &
```
