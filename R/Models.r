# The following are notes from a very helpful PDF book/notebook by Dan Haydon and Darren Shaw at the University of Glasgow

# It is good practice to report both the effect size and an estimate of it's confidence intervals

# Dan Haydon's pdf book on GLMs: There are various R commands that are useful for calculating summaries of fitted values like ggeffects(model, ‘term’)in the package ggpredict, or emmeans(model ~ term) in the package emmeans).

# Again, some notes from Dan Haydon's GLM book: 
#There may be occasions to include a (usually) continuous explanatory
#variable but force the slope to be one. Suppose for example that the volume
#of river water collected in each sample was not exactly the same, but varied
#between say 3 and 7 millilitres. We’d expect the counts of zooplankton in
#these samples to be directly proportional to the volume of water collected.
#Rather than dividing the zooplankton count by the volume and using this
#standardized ‘density per unit volume’ as our response variable, we could
#simply include the volume as an offset and model the counts – a preferable
#strategy as we remain closer to the raw data we actually collected. Offsetting
#is a useful trick, and described in more detail in Appendix J.


# MIXED MODELS

# To fit random effects (e.g. farm, or household - something from which samples have been repeatedly taken, but which we are not directly interested in per se) you will need to use an R package that can cope with this. The R package lme4 can be used, wiht command lmer. 

model_mixed_12.2<-lmer(Chlorophyll ~ Nitrate
+ Flow
+ (1|River),data=my_data)

# the (1|River) includes River as random effect - it will adjust the intercept for each river, based on the variability across all rivers that samples were taken from, but will not produce a coefficient. 

# The output might look like this - note that River, the random effect, has a VARIANCE, not a coefficient. 
Linear mixed model fit by REML.
Formula: Chlorophyll ~ Nitrate + Flow + (1 | River)
Data: my_data
REML criterion at convergence: 327.4
Random effects:
Groups Name Variance Std.Dev.
River (Intercept) 49.07 7.005
Residual 61.79 7.860
Number of obs: 48, groups: River, 4
Fixed effects:
Estimate Std. Error
(Intercept) 15.5964 5.9662
Nitrate 5.2827 0.4452
FlowL -17.8732 2.7860
FlowM -10.3413 2.7932


# If you had non-normal data you could still use the lme4 package but use the glmer model, and specify how the data is distributed.

# If you wanted to see an interaction between the fixed effect, nitrate concentration, and the randome effect, river, in the example above you would write the model as so: 

model_mixed<-lmer(Chlorophyll~Nitrate+Flow+(1+Nitrate|River), data=River_data)

# You would now have a variance for both River and for Nitrate. 

# Important: You decide whether a variable is a Random or a Fixed effect based on whether you are interested in it's effect or not. If not, it is random, if so, use it as a fixed effect, to get the coefficient (the slope with a 1 unit increase for a continuous variable, or the change in intercept with a categorical variable)
