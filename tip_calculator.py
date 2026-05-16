meal = input("How much was the meal? ")
percent = input("what percentage would you like to tip? ")
meal_amount = float(meal[1:])
tip_percent = float(percent[:-1]) / 100
tip_amount = meal * percent
print(f"leave ${tip:.2f}")