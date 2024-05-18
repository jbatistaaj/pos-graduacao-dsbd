2 + 2

x <- 2
y <- 3

x + y

ls()
rm(x)

rm(list= ls())

search()

ls("package:datasets")

WorldPhones <- 10986
WorldPhones

Titanic

getwd()
list.files()

###  
  
base::install.packages("ggplot2")
BiocManager::install()

library(ggplot2)
require(ggplot2)

###

.libPaths()

help(mean)
??mean
?install.packages
RSiteSearch("mean")

###  
  
numeros <- c(1,2,3,4,5)
numeros

letras <- c('a','b','c','d','e')
letras

logicos <- c(TRUE,FALSE,TRUE,FALSE,TRUE)
logicos

vetor <- c(numeros,letras,logicos)
vetor

numeros[1]
letras[3]
logicos[2]
vetor[5]

class(logicos)
class(letras)
class(vetor)

fator = factor(c("Tipo 1",
                 "Tipo 2",
                 "Tipo 3"))
is.factor(fator)

as.numeric(fator)

?methods

methods(class="numeric")

altura <- c("João" = 1.82,
           "Bianca" = 1.68,
           "Eduarda" = 1.62)
class(altura)

attributes(altura)
attributes(numeros)

seq(from = 1, to = 100, by = 5)

seq(from=100, to=1, by= -2)

rep(c(1:3),times = 5)

set.seed(123)
runif(10, min = 0, max = 1)

sample(letras,2)
sample(letras,20,replace=T)

altura <- altura[-2]
altura

