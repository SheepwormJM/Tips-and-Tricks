You can reverse an axis in ggplot2. 

However, I found that some code wouldn't work well...
```
# R v4.4.2, ggplot v3.5.1
# The following would produce a plot with the data reversed but no y-axis ticks
# It didn't seem to matter which way around you put them, or whether you had scale_y_reverse() present or not!
p<-ggplot(data=df, aes(x=POS/1e6, y=value))+
coord_cartesian(ylim=c(57,0),xlim=c(0,49))+
scale_y_reverse()+
scale_y_continuous(
    breaks = seq(0, 57, 10),
    minor_breaks = seq(0, 57, 5)
  )
```
In contrast, this worked, and produced tick marks but I couldn't choose the breaks:
```
# R v4.4.2, ggplot v3.5.1
p<-ggplot(data=df, aes(x=POS/1e6, y=value))+
coord_cartesian(xlim=c(0,49))+
scale_y_reverse()
```
