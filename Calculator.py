print("***BMI Calculator***\n")

Height = input("What is your Height?\n")

Weight = input("What is your Weight?\n")

Height_int = float(Height)

Weight_int = int(Weight)

BMI = Weight_int / (Height_int ** 2)

print("The BMI that you have is " + str(round(BMI ,1)))

print(input("\nClick ENTER to close the window"))