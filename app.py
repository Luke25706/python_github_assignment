#Starting the program
print("Welcome to my Python program!")

#Taking user input
hours = input("How many hours did you study today? ")

#Doing the calculation
hours = float(hours)
weekly_hours = hours * 7

#Displaying the results
print(f"You are on track to study {weekly_hours} hours this week.")

#Basic error handling
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()