class Coffee:
    def __init__(self) -> None:
        self.billAmount = 0
        self.coffeePrices = {
            'Espresso': {
                'Milk': 60,
                'Cream': 75,
                'Latte': 100
            },
            'Cappuccino': {
                'Milk': 80,
                'Cream': 90,
                'Latte': 125
            },
            'Latte': {
                'Milk': 100,
                'Cream': 125,
                'Latte': 150
            }
        }

    def calculateBill(self, Choices) -> int:
        for coffeeType, coffeeAddOns in Choices.items():
            print(coffeeType)
            for addOn, addOnCount in coffeeAddOns.items():
                if addOnCount > 0:
                    addOnPrice = self.coffeePrices[coffeeType][addOn] * addOnCount
                    print(
                        f'\t{addOn}\t {self.coffeePrices[coffeeType][addOn]}\t {addOnCount}\t {addOnPrice}')
                    self.billAmount += self.coffeePrices[coffeeType][addOn] * addOnCount
        return self.billAmount


if __name__ == '__main__':
    coffee = Coffee()
    coffeeType = ['Espresso', 'Cappuccino', 'Latte']
    coffeeAddOns = ['Milk', 'Cream', 'Latte']
    coffeeSummary = {
        'Espresso': {
            'Milk': 0,
            'Cream': 0,
            'Latte': 0
        },
        'Cappuccino': {
            'Milk': 0,
            'Cream': 0,
            'Latte': 0
        },
        'Latte': {
            'Milk': 0,
            'Cream': 0,
            'Latte': 0
        }
    }

    while True:
        try:
            print("Choose coffee type: \n 1. Espresso \n 2. Cappuccino \n 3. Latte")
            coffeeChoice = int(input("Enter here: ")) - 1
            print("Choose addon: \n 1. Milk \n 2. Cream \n 3. Latte")
            addOnChoice = int(input("Enter here: ")) - 1

            if coffeeChoice in [0, 1, 2] and addOnChoice in [0, 1, 2]:
                coffeeSummary[coffeeType[coffeeChoice]
                              ][coffeeAddOns[addOnChoice]] += 1
            else:
                print("Please enter a valid choice (1 or 2 or 3) !!!")
            ans = input("Do you want to add more? (y/n):")[0]
        except:
            print("Please enter a valid choice number !!!")
            ans = input("Do you want to continue? (y/n):")[0]
        if ans == 'n':
            print('\n')
            break

    print("Generated Bill:")
    print("Coffee\t Addon\t Price\t Quantity\t Amount")
    billAmount = coffee.calculateBill(coffeeSummary)
    print("\n\t\tTotal bill amount: ", billAmount, '\n')


'''
Test Case 1 -->
Generated Bill:
Coffee   Addon   Price   Quantity        Amount
Espresso
        Milk     60      5       300
Cappuccino
        Cream    90      1       90
        Latte    125     1       125
Latte
        Cream    125     2       250

                Total bill amount:  765

Test Case 2 -->
Generated Bill:
Coffee   Addon   Price   Quantity        Amount
Espresso
        Milk     60      6       360
Cappuccino
        Cream    90      1       90
        Latte    125     2       250
Latte
        Cream    125     2       250
        Latte    150     1       150

                Total bill amount:  1100
'''
