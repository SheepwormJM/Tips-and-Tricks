## Geom_point, faceted
```
library(ggplot2)
library(reshape2)
library(ggrepel)
library(patchwork)

sessionInfo()

# Loading file
df<-read.table("file", header=F)
head(df)

colnames(df) <- c('chr','mid','MLSUS','MLRES')
summary(df)

# Rename chromosomes to be roman numerals, assuming they are currently called Chr_1 etc:
df$chr<-gsub("Chr_","", df$chr)
df$chr<-gsub("1","I", df$chr)
df$chr<-gsub("2","II", df$chr)
df$chr<-gsub("3","III", df$chr)
df$chr<-gsub("4","IV", df$chr)
df$chr<-gsub("5","V", df$chr)


# melt the table:
df_melt<-melt(df, id.vars=c("chr","mid"))

# Re-order the chromosomes as a factor (to plot roman numerals I-X rather than in alphbetical order)
df_melt$chr <- factor(df$chr, levels=c('I', II', 'III', 'IV', 'V'))

x<- ggplot(data=df_melt, mapping=aes(x=mid, y=value)) +
coord_cartesian(ylim=c(0,1)) +
geom_point(aes(colour=chrom), alpha=0.3, size=0.3) +
labs(y="Genetic differentiation (10kb window Fst)", x="Position in Genome")+
theme_light()+
theme(axis.title.x = element_text(size=10), axis.text.x = element_blank(), axis.title.y = element_text(size=10), axis.text.y = element_text(size=6), strip.text.x = element_text(size = 6, face = "bold", margin = margin(0.5,0,0.5,0, "mm")), strip.text.y = element_text(size = 6, face = "bold", angle=0), plot.title = element_text(size=10, hjust=0.5), legend.position = "bottom", panel.spacing.x = unit(0.2, "mm"), panel.spacing.y = unit(0.75, "mm"))+
facet_wrap(~variable, ncol=3, drop=TRUE)+
guides(colour = guide_legend(override.aes = list(alpha = 1, size=1.5), title = "Chromosome", legend.text.position = "left",  legend.title.position = "top", nrow = 1, legend.text = element_text(size=6), legend.title = element_text(size = 8))) +
ggtitle('F0:F3 generation')

c5<- ggplot(data=subset(win_melt_selpwc, win_melt_selpwc$chrom == "V"), mapping=aes(x=mid/1e6, y=value)) +
coord_cartesian(ylim=c(0,1)) +
scale_x_continuous(
    breaks = seq(0, 55, 10),
    minor_breaks = seq(0, 55, 5)
  )+
scale_y_continuous(
    breaks = seq(0, 1, 0.25)
  )+
geom_point(colour="#619CFF", alpha=0.3, size=0.3) +
labs(y="Genetic differentiation (10kb window Fst)", x="Genomic Position (Mb)")+
geom_hline(yintercept = 0.1840843, linetype = "dashed", linewidth = 0.3, colour = "black") +
geom_hline(yintercept = 0.2144305, linetype = "dotted", linewidth = 0.3, colour = "black") +
theme_light()+
theme(axis.title.x = element_text(size=10), axis.text.x = element_text(size=6), axis.title.y = element_text(size=10), axis.text.y = element_text(size=6), strip.text.x = element_text(size = 6, face = "bold", margin = margin(0.5,0,0.5,0, "mm")), strip.text.y = element_text(size = 6, face = "bold", angle=0), plot.title = element_text(size=10, hjust=0.5), legend.position = "none", panel.spacing.x = unit(0.2, "mm"), panel.spacing.y = unit(0.75, "mm"))+
facet_wrap(~variable, ncol=3, drop=TRUE)+
guides(alpha = "none", colour = "none") +
ggtitle('F3 generation: IVM vs MOX lines')


patchwork <- x3 + c5 
plotme<-patchwork + plot_layout(axis_titles = "collect_y", ncol=2) + plot_annotation(tag_levels = 'A') &
    theme(plot.tag.position = c(0.1, 1))



#ggsave("file.tiff", plotme, device=tiff, width=2250, height=2250, units="px", dpi=320)
ggsave("file.tiff", plotme, device=tiff, width=2250, height=2250, units="px", dpi=320)


```
# To plot different lines on certain variables only (when a faceted plot):
```
geom_hline(data = filter(win_melt_F3.F0, variable==c("IVM1","IVM2", "IVM3")), aes(yintercept = 0.1840843), linetype = "dashed", linewidth = 0.3, colour = "black") +
```
