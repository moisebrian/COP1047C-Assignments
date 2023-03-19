#!/usr/bin/env python3


#20% tax rate
flatTaxRate = 0.20 

# $10,000 tax deduction
standard_deduction = 10000 

# $3,000 deduction per dependent
dependent = 3000

# Gross income in decimal format
gross_income = float(input("Enter the gross income: "))

# number of dependets multipled by the deduction per dependent
number_dependents = int(input("Enter the number of dependents: ")) * dependent


income_tax = ((gross_income - standard_deduction - number_dependents) * flatTaxRate)

#rounds income_tax to two decimal points for acatual money price
incomeTax = round(income_tax,2)

print("The income tax is $", incomeTax)

