# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def karatsuba_mutiplication(x, y):
    xstr = str(x)
    ystr = str(y)
    
    length = max(len(xstr), len(ystr))
    
    
    

    
    if length > 1:
        
        xstr = "0" * (length - len(xstr)) + xstr 
        ystr = "0" * (length - len(ystr)) + ystr
        

        
        xh = int(xstr[:length//2])
        xl = int(xstr[length//2:])
        
        yh = int(ystr[:length//2])
        yl = int(ystr[length//2:])
        
        a = karatsuba_mutiplication(xh, yh)
        d = karatsuba_mutiplication(xl, yl)        
        e = karatsuba_mutiplication(xh + xl, yh + yl) - a - d
        
        base = length - length // 2
        
        xy = a * 10 ** (base * 2) + e * 10 ** base + d
        
        
        return xy
    
    else:

        return int(x) * int(y)

if __name__ == "__main__":
    x = 3141592653589793238462643383279502884197169399375105820974944592
    y = 2718281828459045235360287471352662497757247093699959574966967627
    
    xy = karatsuba_mutiplication(x, y)
    print(xy)
    print(xy - x * y)
        