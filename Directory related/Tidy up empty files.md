```
find . -type f -empty -print 
# The above will print a list of all the empty files to the screen.
Then.... copy and paste the following without the hashtag and it will delete the empty files.
#find . -type f -empty -print -delete # This will delete all the files in the current folder and any other folders within it
#find . -maxdepth 1 f -empty -print -delete # This will only delete the files in the current folder
#find . -maxdepth 1 -type d -empty -print -delete -o -type f -empty -print -delete # This will delete any empty directories OR (-o) any empty files in the current folder.
```
