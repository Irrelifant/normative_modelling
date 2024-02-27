install.packages("gamlss")
library(gamlss)
require(gamlss)
require(ggplot2)


### Does GAMLSS fullfill my assumptions: ?
###### 

### test gamls
data(trees)
model <- gamlss(Volume ~ Girth + Height, data = trees, family = "GA")
summary(model)

###
whole_blood_healthy <- read.csv('whole_blood/whole_blood_combi_reduced.csv')
whole_blood_healthy_wo_meta <- read.csv('whole_blood/whole_blood_combi_reduced_wo_meta.csv')
### Distributional assumption
selected_column_names <- names(whole_blood_healthy.T)[-c(1:7, length(names(whole_blood_healthy.T)))]
selected_column_names
whole_blood_healthy_model <- gamlss(age ~ selected_column_names, data = whole_blood_healthy, family = "GA")

# Summary of the model
summary(whole_blood_healthy_model)

# Diagnostic plots
plot(model)