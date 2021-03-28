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

    print("""
This CLI tool is designed to help you better understand your spending habits.\n
When you input your monthly transactions, we will return how much you spend on
necessities, how much you spend on investments, and how much you spend on entertainment\n
Please input the category and price of your monthly transactions.
If not formated correctly, the input stops:\n
Category options are...
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

    print('')

    while True:

        try:
            category = input("Select a number that corresponds with the category of your purchase (or 'q' to quit): ")
            if category == 'q' or category == 'Q':
                break
            category = int(category)
            while category < 1 or category > 15:
                print("Category must be between 1 and 15")
                category = int(input("Select a number that corresponds with the category or your purchase (or 'q' to quit): "))

            price = float(input(("Category was '" + num_to_cat[category] + "'. Input the price of the purchase: $")))
            while price < 0:
                print("Price must be positive")
                price = float(input(("Category was '" + num_to_cat[category] + "'. Input the price of the purchase: $")))
            calcSum(category, price, num_to_cat)

        except:
            break

    print('')

    total_spending = sumNecessities + sumInvestments + sumEntertainment

    if total_spending == 0:
        print('*' * 35)
        print("You had no treansactions this month")
        print('*' * 35)

    else:
        print('*' * 73)
        print(f"Total spending on necessities was ${round(sumNecessities, 2)} which is {round((sumNecessities/total_spending)*100, 2)}% of all spending")
        print(f"Total spending on investments was ${round(sumInvestments, 2)} which is {round((sumInvestments/total_spending)*100, 2)}% of all spending")
        print(f"Total spending on entertainment was ${round(sumEntertainment, 2)} which is {round((sumEntertainment/total_spending)*100, 2)}% of all spending")
        print('*' * 73)
        print('')
        if min(sumNecessities, sumInvestments, sumEntertainment) == sumNecessities:
            print("Be careful! Make sure you save enough money for the things you need!")
        elif min(sumNecessities, sumInvestments, sumEntertainment) == sumInvestments:
            print("Build for the future! You should spend more on investments (either financial or personal).")
        elif min(sumNecessities, sumInvestments, sumEntertainment) == sumEntertainment:
            print("Treat yourself! You have room in your savings for more consumer goods.")
        print('')

if __name__ == "__main__":
    main()