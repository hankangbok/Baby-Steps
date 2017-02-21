import math

def doafactorial(somenumber,thepower):
    #will hopefully return somenumber!
    total=1
    if somenumber==0:
        return 1
    while somenumber!=0:
        total=total*somenumber
        somenumber=somenumber-1
    print total
    return total

print "Lets test this out"
print doafactorial(5,2)
print doafactorial(0,1)
print doafactorial(4,1)
