```
df<-read.table("MHco20.19.F3_dummyGT.txt", header=T, sep="\t")
summary(df)

# Let's make Genotype_resistance, Boma and Month a factor not a character. And manually order the levels (for plotting):

df$Genotype_resistance<-factor(df$Genotype_resistance, levels = c("S168T","F167Y","E198A","F200Y","S"))
df$Boma<-factor(df$Boma, levels = c("F1R1_MHco2019F3","F2R3_MHco2019F3"))
df$Month<-factor(df$Month, levels = c("April","September"))

# Note - if try to make things factors within the function (i.e. do the above 3 lines within the function below) it doesn't work.

# Also, make the ASV_N a factor. As this is numerical, it should order fine I think:
df$ASV_N<-factor(df$ASV_N)

plot_bar_RRA <- function (my_data, title) {

library(ggplot2)
#library(reshape2)
#library(patchwork)

# And to plot:

# Note that it will seemingly automatically plot the RRA by smallest at the top. Great.
MY_PLOT<- ggplot(data=my_data, mapping=aes(x=Boma, y=RRA, group=Genotype_resistance)) +
geom_bar(mapping=aes(fill=Genotype_resistance), stat="identity", colour="black") +
labs(y="Relative Read Abundance (proportion)", x="Boma", title=paste(title))+
facet_grid(ASV_LOCUS ~ Month)+
scale_fill_manual(name="Genotype", values=c("#CC0000", "#FF3300", "#CC3300", "#990000", "#3399FF"), labels=c("S168T", "F167Y","E198A", "F200Y","Sensitive"))+
theme_bw()+
    theme(plot.title = element_text(size=14), axis.title.x = element_text(size=12), axis.text.x = element_text(size=8), axis.title.y = element_text(size=14), axis.text.y = element_text(size=8), strip.text.x = element_text(size = 10), strip.text.y = element_text(size = 10), legend.position = "top", legend.text = element_text())

invisible(print(MY_PLOT))
}

x<-plot_bar_RRA(df,"MHco20.19.F3_dummyGT")

```
![image](https://github.com/user-attachments/assets/3007519f-6e48-4704-a1ae-ee0bfba9dae0)
