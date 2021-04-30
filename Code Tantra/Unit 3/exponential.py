# WAP to compute the exponential of number w.r.t. another number.

def power(base, exp):
    if(exp == 1):
        return(base)
    if(exp != 1):
        return(base*power(base, exp-1))


base = int(input("Enter Base Number "))
exp = int(input("Enter Exponent Number "))
print(base, "^", exp, "=", power(base, exp))
