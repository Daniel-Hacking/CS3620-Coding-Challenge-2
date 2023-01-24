## Part 1

def BMICalc(weight, height):
    bmi = (weight/height) ** 2
    print(bmi)
    return bmi

weight = int(input("\nPlease enter your weight in Kg : "))
height = int(input("\nPlease enter your height in meters : "))

BMICalc(weight, height)

## Part 2
def divide(a, b):
    if b == 0:
        return "Invalid input"
    return a/b

## Part 3
## Write to file
file = open("demo.txt", "w")
file.write("Demo Text.")
file.close()

## Read File
file = open("demo.txt", "r")
contents = file.read()
print(contents)

## Write code to end of txt file
file = open("demo.txt", "a")
file.write("\nAdditinal Demo Text.")
file.close()

## Part 4
Products = {
    "apple" : 2,
    "car" : 60000,
    "toaster" : 12,
    "house" : 2000000,
    "knowledge" : 0,
}

def checkPrice():
    product = input("Enter the name of the desired product : ")
    return "Price : ${}".format(Products[product.lower()])

print("Products\n")
print("Item")
for i in Products:
    print("{}\n".format(i))
print("\n")
print(checkPrice())
print("\n")


## Part 5
odd = list()
for x in range(100):
    if x % 2 != 0:
        odd.append(x)
        print("{}\n".format(x))
