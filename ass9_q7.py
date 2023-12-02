try:
    a=int(input("Enter the positive value : "))
    if a>0:
          print("You entered correct value")
    else:
        raise ValueError("This is not a positive value")
except ValueError as v:
    print(v)

    
