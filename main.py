necessities = ['Groceries', 'Travel', 'Health', 'Rent', 'Electricity']
investments = ['Fitness', 'Stocks', 'Newsletter Subscriptions', 'Books', 'Technology']
entertainment = ['Dining', 'Alcohol/Beverages', 'Movies', 'Subscriptions', 'Other']

sumNecessities = 0.0
sumInvestments = 0.0
sumEntertainment = 0.0

def calcSum(category, price, num_to_cat):
global sumNecessities
global sumInvestments
global sumEntertainment

if num_to_cat[category] in necessities:
sumNecessities = sumNecessities + price
elif num_to_cat[category] in investments:
sumInvestments = sumInvestments + price

elif num_to_cat[category] in entertainment:
sumEntertainment = sumEntertainment + price

def main():
global sumNecessities
global sumInvestments
global sumEntertainment

print("""This CLI tool is designed to help you see what percentage
of your spending is going to differnt categories.\n
Categories include the following:\n\n
Please input your monthly transactions, if not formated correctly then input stops:\n
Category options are (Input the number):
""")
counter = 1
num_to_cat = {}
for cat in necessities:
num_to_cat[counter] = cat
print(str(counter) + " " + cat)
counter = counter + 1

for cat in investments:
num_to_cat[counter] = cat
print(str(counter) + " " + cat)
counter = counter + 1

for cat in entertainment:
num_to_cat[counter] = cat
print(str(counter) + " " + cat)
counter = counter + 1

while True:
try:
category = input("Select a number that corresponds with the category or your purchase (or 'q' to quit): ")
if category == 'q' or category == 'Q':
break
category = int(category)
while category < 1 or category > 15:
print("Category must be between 1 and 15")
category = int(input("Select a number that corresponds with the category or your purchase: "))
price = float(input(("Input the price of the purchase: $")))
calcSum(category, price, num_to_cat)

except:
break

total_spending = sumNecessities + sumInvestments + sumEntertainment

print(f"Total spending on necessities was ${round(sumNecessities, 2)} which is {round((sumNecessities/total_spending)*100, 2)}% of all spending")
print(f"Total spending on investments was ${round(sumInvestments, 2)} which is {round((sumInvestments/total_spending)*100, 2)}% of all spending")
print(f"Total spending on entertainment was ${round(sumEntertainment, 2)} which is {round((sumEntertainment/total_spending)*100, 2)}% of all spending")

if __name__ == "__main__":
main()
