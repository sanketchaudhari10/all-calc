import math
def calc(should_print=False):
    
    print("""
    Name: std_deviation
    Operation : calculates the standard deviation of a list 
    Inputs : a->List of int\float
    Outputs: b=>int\float
    Author : sanketchaudhari10  
    \n
    """)

    a = list(map(float,input("Enter the numbers: ").split()))

    result = {}
    result['inputs'] = [a]
    
    summation = sum(a)
    mean = summation/max(1,len(a))
    summation = 0
    for i in range(len(a)):
        summation += (mean-a[i])*(mean-a[i])
    
    summation = summation/max(1,len(a))    
    summation = math.sqrt(summation)        
    result['outputs'] = [summation]

    if should_print:
        print(f"Solution {result['outputs'][0]}")
    else:
        return result