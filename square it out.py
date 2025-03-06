def numbers(s, e):
    
    for i in range(s, e + 1):
        
        z = i*i
        
        if z % 2 == 0:
            print(f"i = {i} and square of i = {z} and this is an EVEN NUMBER!")
        else:
            print(f"i = {i} and square of i = {z} and this is an ODD NUMBER!")
        
s = int(input("ENTER THE STARTING POSITION : "))
e = int(input("ENTER THE ENDING POSITION : "))

numbers(s, e)