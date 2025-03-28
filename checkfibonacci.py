def main():
    print("Check - Fibonacci Sequence")
    while True:
        x=input("\nEnter a number to check if the number is part of the fibonacci sequence: ")
        if not(x.isdigit() and int(x)>=0):
            print("Invalid Input!")
        else:
            break
    x=int(x)        
    print(fibonacci(x))           
def fibonacci(x):
    list_fib=[0, 1]
    while list_fib[-1] in range(0, xq1    ):
        k=list_fib[-2]+list_fib[-1]
        list_fib.append(k)        
    if list_fib[-1] == x:
        return f"Number ({x}) is part of the fibonacci sequence!"
    else:
        return f"Number ({x}) is not part of the fibonacci sequence!"    
main()        