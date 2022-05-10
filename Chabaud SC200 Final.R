#Kody Chabaud
#SC200
#Final Assignment 
#Due - 5/10/22
# Rename this file with your last name before submitting.
# By submitting this project you agree you have not violated Southeastern's
# policy on Academic Dishonesty as described on
# the course syllabus.

#Fill in the missing parts below after the instructions in the comments.

#Load any necessary libraries to complete the tasks here.
install.packages("readxl")
library("readxl")
install.packages("PolynomF")
library('PolynomF')
library('foreach')
library('doParallel')
################################################################################
#Module 1 Instructions (5 points.)

#Import the data set g149novickA.xlsx.
my_data <- read_excel("g149novickA.xlsx")
# Column 1 represents the time in hours.
# Column 2 represents the fraction of maximum beta-galactsidase activity.
colnames(my_data) = c("Time in Hours", "Fraction of Maximum")

# Plot the data. Do not connect the points in line segments. Plot the points 
# with a symbol such as a small circle. Add a title and labels for the x 
# and y axes. Make the graph look nice.
plot(x = my_data$`Time in Hours` , y = my_data$`Fraction of Maximum`,
     xlab = "Time in Hours",
     ylab = "Fraction of Maximum Activity",
     main = "Time Vs. Fraction of Maximum",
     col = 'purple'
)
################################################################################

# Module 3 (10 points)
#Use least squares to determine the parameter a for a model of the form
# V(t) = 1 - exp(-t/a).
# Ensure you know to do the fit to the data set from the imported file g149novickA.xlsx.
x <- my_data$`Time in Hours`
y<- my_data$`Fraction of Maximum`
plot(x,y, pch = 16, col ="blue", main = 'Nonlinear')
grid(nx = NULL, ny = NULL)
df <- data.frame(x,y)
model <- nls(y ~ 1-exp(-x/a), data = df, start = c(a = 1))
model
x2 = seq(0, 7, by = 0.1)
yFit <- 1-exp(-x2/a)
lines(x2, yFit)
a <- coef(model)
residuals(model)
sumRes <- sum(abs(residuals(model)))
sumRes

# Print a.
print(a)
# Plot the model as a smooth continuous curve on top of the data set.
#!!already plotted above!!

# Obtain an approximation at t = 5.5 hours.
t5.5 <- 1-exp(-5.5/a)
# Print the approximation.
print(t5.5)



#In the same figure window (but with a different color), plot a new model 
# using NATURAL cubic splines on top of the data set from the polynomF package.
#Print the approximation for t = 5.5 with the cubic spline model.
#Add a legend, i.e.
#legend("bottomright", c('Data', 'Least Squares', 'Cubic Splines'), col = c("black", "black", "red"), lty = c(3,1,1))

model2 = splinefun(x,y, method = "natural")
model2
print(model2(5.5))
plot(model2(x),model2(y))
legend("bottomright", c('Data', 'Least Squares', 'Cubic Splines'), col = c("black", "black", "red"), lty = c(3,1,1))

################################################################################
#Module 5 (10 points)
# Create a function multiply that takes an input, i, generates a random number j 
# between 0 and 1 and returns i*j.
multiply <- function(i){
  #i <- readline(prompt="i =  ")
  j <- runif(1,0,1)
  return(i*j)
}
x <- 5
multiply(x)
# Create an EMPTY matrix M of size rows = 30, cols = 20
M <- matrix(nrow = 30, ncol = 20)

#Fill in the matrix M in parallel using a nested foreach loop for i = 1:rows

M <- foreach(i = 1: 30) %dopar% sqrt(i)
#print the filled in matrix
print(M)


