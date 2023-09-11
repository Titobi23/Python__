# Compound Interest Calculator

initialInvestment = int(input("How much are you going to invest? "))
term = int(input("How many years are you going to invest your money? "))
interestRate = float(input("Input the annual interest rate as a decimal.  [For 2% enter .02] "))

x = 1
print("Month \t Interest Earned \t Total")
while x < (term * 12 + 1):
    interestEarned = initialInvestment * (interestRate / 2)
    initialInvestment = interestEarned + initialInvestment
    print(x, "\t", "$", "{:.2f}".format(interestEarned), "\t", "$", "{:.2f}".format(initialInvestment))
    x = x + 1