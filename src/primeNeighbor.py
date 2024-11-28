'''
Created by Neda Topuz
Modified by Atalay Akgul
'''

def primeNeighbor(upperBound):
    if not isinstance(upperBound, int) or upperBound <= 1 or upperBound > 1000:
        return 0  

    def is_prime(num):
        """Check if a number is prime."""
        if num <= 1:
            return False
        if num == 2:  
            return True
        if num % 2 == 0:  
            return False
        for i in range(3, int(num**0.5) + 1, 2):  
            if num % i == 0:
                return False
        return True
    
    
    for num in range(upperBound, 1, -1):
        if is_prime(num):
            return num  

    return 0  
