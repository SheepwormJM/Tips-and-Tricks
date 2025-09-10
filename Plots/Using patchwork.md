Patchwork is a great tool that lets you group ggplots together. https://patchwork.data-imaginist.com/index.html

Things to note/things that cause errors:

1. Adding tags to plots:
```
# To manipulate the location of the plot tags (A, B, C etc) then you need to add the theme(plot.tag.position()).
# Note that there is an & rather than a + between the theme and the rest - not sure if this is important, but this is how I found it and have used it
# Note that the plot.tag.position doesn't seem to work unless you also include the ncol in the plot_layout
# Note that the co-ordinates are x,y for the plot.tag.position, but that the outcome may vary between plots!

patch<- p1 + p2 + p3 + p4 + plot_annotation(tag_levels = 'A') + plot_layout(axis_titles = "collect", ncol=2) & theme(plot.tag = element_text(size = 15), plot.tag.position = c(0.1, 1))
patch
```
