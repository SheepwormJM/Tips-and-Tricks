Instead of using ```write.table()``` you can create a binary R object file, which can then be usfully reloaded later if your script fails on memory, time or code!

To make the object file: 
```
# Let's say I've just made a somthing called p_values_MC that contains some results I've just calculated in R....

# Make an binary Robject file that could be easily reloaded if desired to replot the plot!

save(p_values_MC, file="filename.obj")
```
To then reload this, e.g. to tweak the script and replot your plot that isn't quite right... 
```
load("filename.obj")
```
Note that you cannot do this: 
```
df<-load("filename.obj")
```
As it will fail. When you simply do the load() then it will load the file as a tibble and also call it whatever it was originally called in R. So the example above would be your data reloaded as p_values_MC. 
