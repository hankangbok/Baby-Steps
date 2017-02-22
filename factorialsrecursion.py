def factorial(whatnumber):
    if whatnumber<1:
        return 1
    else:
        result=whatnumber*factorial(whatnumber-1)
        return result

print factorial(4)
print factorial(0)
