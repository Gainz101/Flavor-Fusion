# Start of Python file

# Create a list of food items
foods = ["Pizza", "Burger", "Pasta", "Sushi", "Tacos", "Salad", "Steak", "Ice Cream", "Donuts", "Fries"]

# Create an empty list to store the ratings
ratings = []

# Ask the user to rate each food
for food in foods:
    while True:
        try:
            rating = int(input(f"On a scale of 1-10, how much do you like {food}? "))
            if 1 <= rating <= 10:
                ratings.append(rating)
                break
            else:
                print("Invalid input. Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Print out the ratings
print("Your food ratings are:", ratings)

# End of Python file
