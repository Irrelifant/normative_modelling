install.packages("jsonlite")
install.packages("gamlss")
library(gamlss)
require(gamlss)
require(ggplot2)

### Does GAMLSS fullfill my assumptions: ?
###### distribution -> 10k_immu

###
whole_blood_healthy <- read.csv('whole_blood/whole_blood_combi_reduced.csv')
whole_blood_healthy_wo_meta <- read.csv('whole_blood/whole_blood_combi_reduced_wo_meta.csv')
#TODO train test split
whole_blood_healthy_wo_meta

### to model in gamells:
# technik:  marray RNAseq. 
# platform: hiseq, .... illumina...
# studie 
# age, sex
## 1 model: age
## 1 model: sex
## 1 model: age, sex
## dann das mit einzelnen korrektur variablen
#### platform, technik, studie.

# evtl qualität ??
# was halt sinn macht

### Distributional assumption
selected_column_names <- names(whole_blood_healthy.T)[-c(1:7, length(names(whole_blood_healthy.T)))]
selected_column_names

whole_blood_healthy_model <- gamlss('DUSP22' ~ age + gender, data = whole_blood_healthy, family = "GA")

# Summary of the model
summary(whole_blood_healthy_model)

# Diagnostic plots
plot(model)