args <- commandArgs(trailingOnly = TRUE)
# args[1] = the input table
# args[2] = the output table
# args[3] = the name of the pdf with the plot

setwd(getwd())

data <- read.table(args[1], header=TRUE, sep = ",")
data$rand <- data$age + runif(30) / data$year
write.csv(data, file=args[2], row.names=FALSE)

pdf(file=args[3])
plot(data$rand, pch=19, col="blue")
dev.off()