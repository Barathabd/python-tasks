print("Welcome to the rollercoaster!")
Height=float(input("What is your height?\n"))
if (Height>=120):
    print("You can ride the roller coaster")
    Age=int(input("Please enter your age:"))
    if (Age<12):
        Bill=5
    elif(Age<=18):
        Bill=7
    else:
        Bill=12
    Want_photos=input("Do you want photos? yes or no :")
    if ("yes"):
        Bill+=3
        print(f"your final bill is {Bill}")
else:
    print("You need to grow up to ride rollercoaster")