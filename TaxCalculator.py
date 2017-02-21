import math
import sys
#def taxcalculator(cost,taxpercentage):
#    print "Please enter the cost and tax as a decimal"
#    return round(cost+cost*taxpercentage,2)

def taxcalculator():
    cost=float(raw_input("how much was the item you bought? "))
    tax=float(raw_input("What is the tax? Please enter it as a decimal:"))
    return round(cost+cost*tax,2)
print taxcalculator()
print taxcalculator()
