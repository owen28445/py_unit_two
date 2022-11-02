

names = (input("it's so nice to meet you, what is your name?"))

print("It's so nice to meet you",names)
print ("my name is chatbot")

location = (input("where do you live?"))

print(location, "sounds like a pleasant place to be from")

numbers = int((input("what is your favorite number?")))

theDifference =  (numbers - 7 )

print("the difference between your number and my number is", theDifference)

car = (input("what is your dream car"))

print("Wow, I've always wanted a",car, "as well")



costs = int(input("how much does the car costs."))

print("Wow, that is expensive.")

loan = int(input("how many years do user would take to pay the car"))

interestrate = float(input("the interest rate is "))

r = interestrate/100/12
p = costs
n = loan*12

print(r,"is the monthly rate")
print(p," is the cost")
print(n, " is the number of months of the loan")

mpymt = (r * p) / ((1 - ( 1 + r) ** -n))
print("mothly payment is", mpymt)


print("I hope you can make the purchase!Anyways, I gotta go. It's been nice chattin' with ya Jane Student")

print("goodbye Owen")






