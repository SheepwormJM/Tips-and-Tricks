# Add line numbers: 
### ...which can handily give a rank after first sorting a file:
- Note, these are always added in a new first column/start of the file.

Nice bit of info here: https://www.geeksforgeeks.org/nl-command-in-linux-with-examples/ 
```
cat file | sort -k 4 -n | nl > new_file
```
