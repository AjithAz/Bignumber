a = int(input("Enter the First number:"))
b = int(input("Enter the Second number:"))
c = int(input("Enter the Third number:"))

if a > b and a > c:
    print("First Number is Big")
elif b > a and b > c:
    print("Second Number is Big")
elif c > a and c > b:
    print("Third Number is Big")
else:
    print("All are equal")
