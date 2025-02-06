1. Find command:
```
find <directory-to-start-search-in> -name <filename>

find . -name POVIS
```

Note:
1. Using the above command as is will not search through symbolic links
2. Using the above command as is will search through all subdirectories within the folder
3. Using teh above command as is will identify both files and directories
4. You can specificy to search to a ```-maxdepth```, for just directories or files ```-type```.
