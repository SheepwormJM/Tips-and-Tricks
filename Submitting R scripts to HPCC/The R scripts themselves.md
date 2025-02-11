Note, I found various websites helpful for this, but particularly this one: 
https://www.r-bloggers.com/2015/09/passing-arguments-to-an-r-script-from-command-lines/

For ease of understanding how to write your script (below, 'my_r_script.sh') know that when you submit it to the cluster you will have a command which says basically: 
```
Rscript ./my_r_script.sh  argument_1 argument_2 ... argument_n
```

1. Start your Rscript with a line telling it what it is: 
```
#!/usr/bin/env Rscript
```
2. When you submit your rscript it will be really cool and useful if you can submit it for multiple different files, so you don't need to change it each time. For this you need to have the ability to pass specific arguments to the rscript in the command line when you submit it -  and for your Rscript to then pick these up!

I found that the initial code I used for this didn't work. However, this did, so add this bit next to your Rscript. The trailingonly = TRUE means that it will only look for argument commands after the ```Rscript ./my_rscript.sh```. 

The website also had a nice bit to check that there were arguments and you hadn't forgotten them! And to create a default output file if you had only given a single argument. 
```
args = commandArgs(trailingOnly=TRUE)

# test if there is at least one argument: if not, return an error
if (length(args)==0) {
  stop("At least one argument must be supplied (input file).n", call.=FALSE)
} else if (length(args)==1) {
  # default output file
  args[2] = "out.txt"
}
```

3. Convert your arguments into nice names in the script (this is optional, there are other ways - see the website above, but I like this):
```
input_path = args[1]
input_file = args[2]
output_file = args[3]
```
4. Write in your code. For example, here I load an (unused) library, then first load my input file, summarise the contents and write these to a new output file. 
```
library(ggplot2)

df<- read.delim(paste(input_path,input_file, sep="")) # Note, without the sep="" it adds a space between the path and the file, real pest!
dfsum<-summary(df)
write.table(dfsum, file=paste(output_file,".txt",sep=""), row.names=FALSE, sep="\t", quote= FALSE) 
```

# my_r_script.sh 
```
#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)

# test if there is at least one argument: if not, return an error
if (length(args)==0) {
  stop("At least one argument must be supplied (input file).n", call.=FALSE)
} else if (length(args)==1) {
  # default output file
  args[2] = "out.txt"
}

input_path = args[1]
input_file = args[2]
output_file = args[3]

library(ggplot2)

df<- read.delim(paste(input_path,input_file, sep="")) # Note, without the sep="" it adds a space between the path and the file, real pest!
dfsum<-summary(df)
write.table(dfsum, file=paste(output_file,".txt",sep=""), row.names=FALSE, sep="\t", quote= FALSE)
```
Note that it seems that all the stuff that would usually be printed to your screen in R is instead put into the slurm logfiles. 
